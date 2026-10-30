"""Shared helpers for the EX era (Ruby & Sapphire through Power Keepers).

Card scripts stay thin data definitions; put non-trivial EX-era behavior here
so reprints across EX / Nintendo promos / POP can import the same effect.

Era themes: Pokémon-ex (2 prizes via subtype ``ex``), Poké-Powers / Poké-Bodies,
dual types, δ Delta Species, Holon Energies, Pokémon Star, Dark / owner's /
Rocket's Pokémon.
"""

from __future__ import annotations

import random
from typing import Any, Callable, Optional

from spirit.game.attributes import (
    AbilityTypes, AttrID, PokemonStage, PokemonTypes, SpecialConditions, TrainerType,
)
from spirit.game.card_effects.attacks_common import (
    count_energy, count_prizes_remaining, damage_per, discard_random_from_hand,
    lock_all_attacks,
)
from spirit.game.card_effects.passives_common import (
    apply_own_next_turn_boost, is_in_active_spot, prevent_damage_when,
    retreat_discount, retreat_free_when, takes_less_passive,
    team_damage_boost_passive,
)
from spirit.game.card_effects.pokemon import (
    devolvable, energy_provides_type, is_energy_card,
)
from spirit.game.card_effects.support_common import opponent_switches, search_to_bench
from spirit.game.card_effects.trainers import FossilBodyPassive, is_basic_energy_card
from spirit.game.data_utils import TRAINER_EFFECTS_BY_GUID, def_for, subtypes_for, unimplemented
from spirit.game.session.effects import (
    full_stack, is_basic_pokemon, is_evolution_pokemon, is_pokemon_card,
    is_supporter_card,
)
from spirit.game.session.passives import (
    Passive, TurnDamageModifier, carrier_pokemon, effective_max_hp,
    effective_pokemon_types,
)

# Prefer attacks_common / support_common / trainers / passives_common from call
# sites; add EX-specific factories below as sets need them.


def poke_power_condition(extra: Optional[Callable] = None):
    """Poké-Powers can't be used while the Pokémon has a Special Condition.

    `extra` is an additional (board, player_id, pokemon) playability check
    composed after the Special Condition block.
    """
    def check(board, player_id, pokemon=None):
        if pokemon is not None and pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
            return False
        return extra is None or extra(board, player_id, pokemon)
    return check


def _energy_in_hand(board, player_id, pokemon=None) -> bool:
    hand = board.find_player_area(player_id, "hand")
    return any(is_energy_card(c) for c in (hand.children if hand else []))


def has_deck(board, player_id, pokemon=None) -> bool:
    area = board.find_player_area(player_id, "deck")
    return bool(area) and bool(area.children)


energy_draw_condition = poke_power_condition(_energy_in_hand)


def energy_draw(max_cards: int = 3):
    """Discard 1 Energy from hand, then draw up to `max_cards` (Energy Draw)."""
    async def effect(ctx):
        discarded = await ctx.discard_from_hand(
            1, predicate=is_energy_card,
            prompt="Discard 1 Energy card from your hand",
        )
        if not discarded:
            return
        available = min(max_cards, len(ctx.deck()))
        if available <= 0:
            return
        n = await ctx.choose(
            "Draw how many cards?",
            [str(i) for i in range(available + 1)],
            use_panel=False,
        )
        if n > 0:
            await ctx.draw_cards(n)
    return effect


def attach_from_discard_then_counters(predicate=None, count: int = 2,
                                      counters_per: int = 1, prompt: str = ""):
    """Attach up to `count` matching Energy from discard to 1 of your Pokémon,
    then put `counters_per` damage counters on it for each card attached
    (Pichu Energy Retrieval)."""
    pred = is_basic_energy_card if predicate is None else predicate

    async def effect(ctx):
        cards = [c for c in ctx.discard_pile() if pred(c)]
        if not cards:
            return
        picks = await ctx.choose_cards(
            cards, count, minimum=0,
            prompt=prompt or "Choose basic Energy cards to attach.",
        )
        if not picks:
            return
        candidates = ctx.my_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose a Pokémon to attach the Energy to",
        )
        if target is None:
            target = candidates[0]
        if target.entity_id not in ctx.visual_targets:
            ctx.visual_targets.append(target.entity_id)
        for card in picks:
            await ctx.attach_energy(card, target)
        await ctx.deal_damage(
            len(picks) * counters_per * 10, target=target,
            apply_modifiers=False, as_counters=True,
        )
    return effect


def search_attach_then_counters(predicate, counters: int = 2, prompt: str = ""):
    """Search the deck for an Energy, attach it to 1 of your Pokémon, put
    `counters` damage counters on that Pokémon, then shuffle (Psy Shadow)."""
    async def effect(ctx):
        picks = await ctx.search_deck(
            predicate, count=1, minimum=0,
            prompt=prompt or "Choose an Energy card to attach.",
        )
        if picks:
            candidates = ctx.my_pokemon_in_play()
            if candidates:
                target = await ctx.choose_pokemon(
                    candidates, "Choose a Pokémon to attach the Energy to",
                )
                if target is None:
                    target = candidates[0]
                if target.entity_id not in ctx.visual_targets:
                    ctx.visual_targets.append(target.entity_id)
                await ctx.attach_energy(picks[0], target)
                await ctx.deal_damage(
                    counters * 10, target=target,
                    apply_modifiers=False, as_counters=True,
                )
        await ctx.shuffle_deck()
    return effect


def natural_cure_on_attach(energy_type):
    """Poké-Body: attaching an Energy of `energy_type` from hand cures this Pokémon."""
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        if ctx.attaching_player_id != ctx.player_id \
                or ctx.energy_receiver is not ctx.source:
            return
        energy = ctx.attached_energy
        if energy is None or not energy_provides_type(energy, type_value):
            return
        await ctx.cure_all_conditions(ctx.source)
    return effect


class FlipReduceDamagePassive(Passive):
    """Hard Cocoon: if this Pokémon would be damaged by an opponent's attack
    (after Weakness and Resistance), flip a coin. Heads reduces that damage
    by `amount`."""

    def __init__(self, amount, title=""):
        self.amount = amount
        self.title = title

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if carrier_pokemon(carrier) is not target:
            return None
        heads = await ctx.flip_coins(
            1, self.title, source=carrier_pokemon(carrier) or carrier)
        if heads and heads[0]:
            return max(0, calc.amount - self.amount)
        return None


def flip_reduce_damage_passive(amount, title="") -> Passive:
    """Flip-to-reduce shield: heads takes `amount` less from the attack hit."""
    return FlipReduceDamagePassive(amount, title)


def is_pokemon_ex(card) -> bool:
    """True when `card` is a Pokémon-ex (subtype ``ex``)."""
    return card is not None and "ex" in subtypes_for(
        getattr(card, "archetype_id", None) or ""
    )


def defender_is_ex(ctx) -> bool:
    """cond_fn: the Defending Pokémon is a Pokémon-ex (subtype ``ex``)."""
    return is_pokemon_ex(ctx.defender)


class SafeguardExPassive(Passive):
    """Prevent all effects of attacks, including damage, done to this
    Pokémon by the opponent's Pokémon-ex (Safeguard)."""

    def prevents_damage(self, calc, carrier):
        return (
            calc.is_attack
            and calc.is_opposing
            and carrier_pokemon(carrier) is calc.target
            and is_pokemon_ex(calc.attacker)
        )

    def blocks_attack_effects_from(self, target, carrier, attacker):
        return (
            carrier_pokemon(carrier) is target
            and is_pokemon_ex(attacker)
        )


def safeguard_ex_passive() -> Passive:
    """Poké-Body: immune to attacks from Pokémon-ex (Safeguard)."""
    return SafeguardExPassive()


def extra_energy_damage(per: int, base: int = 0, extra_cap: Optional[int] = None,
                        energy_type=None):
    """`base` + `per` for each Energy attached beyond this attack's Energy cost.

    extra_cap limits leftover Energy counted (Energy Ball's "can't add more
    than 20" is extra_cap=2 with per=10). energy_type counts only that type
    after paying its typed cost and Colorless slots (Water Gun).
    """
    count_attached = count_energy("self", energy_type=energy_type)
    type_value = getattr(energy_type, "value", energy_type)
    colorless = PokemonTypes.COLORLESS.value

    async def effect(ctx):
        attached = count_attached(ctx)
        cost = getattr(ctx.ability, "cost", None) or {}
        if type_value is None:
            paid = sum(cost.values())
        else:
            paid = 0
            for energy, n in cost.items():
                paid_type = getattr(energy, "value", energy)
                if paid_type == type_value or paid_type == colorless:
                    paid += n
        extra = max(0, attached - paid)
        if extra_cap is not None:
            extra = min(extra, extra_cap)
        amount = base + per * extra
        if amount > 0:
            await ctx.deal_damage(amount)
    return effect


def life_drain(flip: bool = True):
    """Flip (default): put damage counters on the Defending Pokémon until it
    is 10 HP away from being Knocked Out. No-ops when remaining HP is 10 or
    less (counters only; never heals)."""
    async def effect(ctx):
        if flip:
            results = await ctx.flip_coins(
                1, ctx.ability.title if ctx.ability else "")
            if not results or not results[0]:
                return
        defender = ctx.defender
        if defender is None:
            return
        amount = defender.get_attribute(AttrID.HP, 0) - 10
        if amount > 0:
            await ctx.deal_damage(amount, as_counters=True)
    return effect


def _named(name: str):
    def pred(card) -> bool:
        return getattr(def_for(card.archetype_id), "display_name", None) == name
    return pred


def search_evolution_pair(*pairs):
    """Search the deck for 1 card or both cards of one named pair, reveal,
    put into hand, and shuffle (Wurmple Signs of Evolution)."""
    async def effect(ctx):
        labels = [" and ".join(pair) for pair in pairs]
        idx = await ctx.choose("Search for which evolution pair?", labels)
        names = pairs[idx]
        picked = await ctx.search_deck_groups(
            [(_named(name), 1, f"Choose a {name}") for name in names],
            prompt="Choose 1 card or both cards of the pair.",
        )
        await ctx.put_in_hand(
            [card for group in picked for card in group], reveal=True)
        await ctx.shuffle_deck()
    return effect


async def lady_outing(ctx):
    """Search the deck for up to 3 basic Energy of different types, show
    them, put them into your hand, and shuffle."""
    deck_cards = list(ctx.deck(ctx.player_id))
    reps = []
    seen_types = []
    for card in deck_cards:
        if not is_basic_energy_card(card):
            continue
        types = card.get_attribute(AttrID.POKEMON_TYPES) or []
        if not types or types[0] in seen_types:
            continue
        seen_types.append(types[0])
        reps.append(card)
    picks = await ctx.choose_cards(
        reps, 3, minimum=0,
        prompt="Choose up to 3 basic Energy cards of different types.",
        display_cards=deck_cards,
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


def heal_each_except_user(amount: int):
    """Heal `amount` from each of your Pokémon except the attacker (Healing Egg)."""
    async def effect(ctx):
        for pokemon in ctx.my_pokemon_in_play():
            if pokemon is ctx.attacker:
                continue
            await ctx.heal(amount, pokemon)
    return effect


def increased_base_damage_next_turn(*boosts):
    """During your next turn, named attacks on this Pokémon do +N.

    Each argument is ``(attack_title, extra_damage)`` (Pelipper Stockpile).
    """
    async def effect(ctx):
        for title, amount in boosts:
            await apply_own_next_turn_boost(ctx, amount, title)
    return effect


def heal_equal_to_damage():
    """Deal printed damage, then heal this Pokémon by the damage done to
    the Defending Pokémon (Swallow / Giga Drain)."""
    async def effect(ctx):
        dealt = await ctx.deal_damage()
        if dealt > 0:
            await ctx.heal(dealt, target=ctx.attacker)
    return effect


def scoop_defending_to_hand(flip: bool = False):
    """Return the Defending Pokémon and all attached cards to the opponent's
    hand. Does nothing without a Benched Pokémon to promote. flip=True
    gates the scoop on heads (Nosepass Repulsion)."""
    async def effect(ctx):
        if not ctx.opponent_bench():
            return
        if flip:
            results = await ctx.flip_coins(
                1, ctx.ability.title if ctx.ability else "")
            if not results or not results[0]:
                return
        target = ctx.defender
        if target is None or ctx.effects_blocked(target):
            return
        await ctx.put_in_hand(full_stack(target), reveal=False)

        async def _promote():
            if not await ctx.session._promote_new_active(ctx.opponent_id):
                screen_name = ctx.session.players[ctx.opponent_id].screen_name
                await ctx.session.end_game(
                    ctx.player_id, f"{screen_name} has no Pokémon left")

        ctx.deferred_actions.append(_promote)
    return effect


class TeamTakesLessBeforeWRPassive(Passive):
    """While the carrier is Active, opponent attacks deal `amount` less to
    the carrier owner's Pokémon (before Weakness and Resistance)."""

    def __init__(self, amount: int, while_active: bool = True):
        self.amount = amount
        self.while_active = while_active

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if self.while_active and not is_in_active_spot(carrier):
            return
        if calc.target.owning_player_id != carrier.owning_player_id:
            return
        calc.amount = max(0, calc.amount - self.amount)


def team_takes_less_before_wr(amount: int, while_active: bool = True) -> Passive:
    """Mightyena Intimidating Fang shape: as long as this Pokémon is Active,
    your Pokémon take N less from opponent attacks (before W/R)."""
    return TeamTakesLessBeforeWRPassive(amount, while_active)


def flip_discard_random_from_opponent_hand(count: int = 1):
    """Printed damage; flip a coin. If heads, discard `count` random cards
    from the opponent's hand without looking."""
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if results and results[0]:
            await discard_random_from_hand(
                ctx, player_id=ctx.opponent_id, count=count)
    return effect


def rough_skin(counters: int = 1):
    """Poké-Body: if this Active Pokémon is damaged by an opponent's attack
    (even if Knocked Out), put `counters` damage counters on the attacker."""
    async def effect(ctx):
        pokemon = ctx.source
        if not is_in_active_spot(pokemon):
            return
        attacker = ctx.damaged_by
        if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
            return
        await ctx.deal_damage(
            counters * 10, target=attacker,
            apply_modifiers=False, as_counters=True,
        )
    return effect


def attached_basic_energy_at_least(n: int):
    """Attack condition: this Pokémon has at least `n` basic Energy cards."""
    def check(board, player_id, pokemon) -> bool:
        return sum(1 for c in pokemon.children if is_basic_energy_card(c)) >= n
    return check


def discard_basic_energy_attack(count: int = 1, also=None):
    """Deal printed damage, then discard `count` basic Energy cards from the
    user. Pair with ``attached_basic_energy_at_least`` so the attack is not
    offered (and therefore does nothing) without enough Energy."""
    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.discard_energy_from(
            ctx.attacker, count, predicate=is_basic_energy_card,
            prompt="Discard basic Energy from this Pokémon",
        )
        if also is not None:
            await also(ctx)
    return effect


async def lock_own_attacks(ctx):
    """This Pokémon can't attack during your next turn."""
    if ctx.attacker is not None:
        lock_all_attacks(ctx, ctx.attacker)


class OpponentPokePowerLockPassive(Passive):
    """While the carrier is Active, the opponent's Pokémon can't use
    Poké-Powers (Slaking Lazy). Poké-Bodies stay on."""

    def blocks_ability(self, pokemon, ability, carrier):
        if not is_in_active_spot(carrier):
            return False
        if pokemon.owning_player_id == carrier.owning_player_id:
            return False
        return getattr(ability, "ability_type", None) == AbilityTypes.POKE_POWER


def opponent_poke_power_lock() -> Passive:
    """Lazy shape: as long as this Pokémon is Active, the opponent's
    Pokémon can't use Poké-Powers."""
    return OpponentPokePowerLockPassive()


def attach_from_hand(predicate, target="active", prompt: str = "",
                     counts_as_attachment: bool = True):
    """Attach 1 matching Energy from hand. target 'active' or 'choice'.

    counts_as_attachment=True so "from your hand" Poké-Bodies (Natural Cure /
    Natural Remedy) observe the attach.
    """
    async def effect(ctx):
        cards = [c for c in ctx.hand() if predicate(c)]
        if not cards:
            return
        picks = await ctx.choose_cards(
            cards, 1, prompt=prompt or "Choose an Energy card to attach.",
        )
        if not picks:
            return
        if target == "active":
            receiver = ctx.my_active()
        else:
            candidates = ctx.my_pokemon_in_play()
            if not candidates:
                return
            receiver = await ctx.choose_pokemon(
                candidates, "Choose a Pokémon to attach the Energy to")
        if receiver is None:
            return
        if receiver.entity_id not in ctx.visual_targets:
            ctx.visual_targets.append(receiver.entity_id)
        await ctx.attach_energy(
            picks[0], receiver, counts_as_attachment=counts_as_attachment)
    return effect


def heal_on_attach(energy_type, amount: int = 10, once_per_turn: bool = True):
    """Poké-Body: attaching an Energy of `energy_type` from hand heals
    `amount` from this Pokémon (Natural Remedy)."""
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        if ctx.attaching_player_id != ctx.player_id \
                or ctx.energy_receiver is not ctx.source:
            return
        energy = ctx.attached_energy
        if energy is None or not energy_provides_type(energy, type_value):
            return
        if once_per_turn:
            used_key = (
                ctx.source.entity_id,
                ctx.ability.ability_id if ctx.ability else "heal_on_attach",
            )
            if used_key in ctx.session.turn_state.used_abilities:
                return
            ctx.session.turn_state.used_abilities.add(used_key)
        await ctx.heal(amount, ctx.source)
    return effect


def heal_all_and_cant_attack():
    """Remove all damage from this Pokémon; it can't attack next turn
    (Slack Off)."""
    async def effect(ctx):
        pokemon = ctx.attacker or ctx.source
        if pokemon is not None:
            missing = ctx.max_hp(pokemon) - pokemon.get_attribute(AttrID.HP, 0)
            if missing > 0:
                await ctx.heal(missing, pokemon)
            lock_all_attacks(ctx, pokemon)
    return effect


def flip_tails_discard_energy(energy_type=None, all_energy: bool = False):
    """Printed damage; flip a coin. If tails, discard 1 Energy of
    `energy_type` (or any Energy) from this Pokémon (Fireworks).
    all_energy=True discards every matching Energy card (Burn Up)."""
    type_value = getattr(energy_type, "value", energy_type)
    pred = (lambda c: energy_provides_type(c, type_value)) \
        if type_value is not None else None

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if results and not results[0]:
            await ctx.discard_energy_from(
                ctx.attacker, 99 if all_energy else 1, predicate=pred,
                prompt="Discard Energy from this Pokémon",
            )
    return effect


def energy_trans_condition(energy_type=PokemonTypes.GRASS):
    """Poké-Power: at least 2 of your Pokémon in play, and one has an Energy
    providing `energy_type` that can be moved (Energy Trans)."""
    type_value = getattr(energy_type, "value", energy_type)

    def extra(board, player_id, pokemon=None):
        in_play = board.pokemon_in_play(player_id)
        if len(in_play) < 2:
            return False
        return any(
            energy_provides_type(e, type_value)
            for p in in_play for e in p.children
        )
    return poke_power_condition(extra)


def energy_trans(energy_type=PokemonTypes.GRASS):
    """Move 1 Energy providing `energy_type` from one of your Pokémon to
    another (Energy Trans). Pair with ``Activations.UNLIMITED``."""
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        pokemon = ctx.my_pokemon_in_play()
        await ctx.move_energy_freely(
            pokemon, pokemon,
            predicate=lambda c: energy_provides_type(c, type_value),
            max_count=1,
        )
    return effect


def attach_energy_from_hand(predicate=None, count: int = 1, prompt: str = ""):
    """Attach up to `count` matching Energy cards from hand to your Pokémon
    (Plus Energy). `predicate` defaults to basic Energy."""
    pred = is_basic_energy_card if predicate is None else predicate

    async def effect(ctx):
        energies = [c for c in ctx.hand() if pred(c)]
        take = min(count, len(energies))
        if take <= 0:
            return
        picks = await ctx.choose_cards(
            energies, take, minimum=take,
            prompt=prompt or "Choose a basic Energy card to attach.",
        )
        for card in picks:
            candidates = ctx.my_pokemon_in_play()
            if not candidates:
                return
            target = await ctx.choose_pokemon(
                candidates, "Choose a Pokémon to attach the Energy to",
            )
            if target is None:
                target = candidates[0]
            await ctx.attach_energy(card, target)
    return effect


def _pokenav_match(card) -> bool:
    return is_basic_pokemon(card) or is_evolution_pokemon(card) or is_energy_card(card)


async def poke_nav(ctx):
    """Look at the top 3 cards; put 1 Basic Pokémon, Evolution, or Energy
    into your hand (show it); put the rest back on top in any order."""
    top = ctx.deck_top(3)
    if not top:
        return
    candidates = [c for c in top if _pokenav_match(c)]
    picks = []
    if candidates:
        picks = await ctx.choose_cards(
            candidates, 1, minimum=1,
            prompt="Choose a Basic Pokémon, Evolution card, or Energy card.",
            display_cards=top,
        )
        await ctx.put_in_hand(picks, reveal=True)
    remaining = len(top) - len(picks)
    if remaining > 1:
        await ctx.reorder_deck_top(remaining)


def lizard_poison():
    """Printed damage, then Asleep / Poisoned / Burned from attached Energy
    count (Sceptile Lizard Poison)."""
    count_attached = count_energy("self")

    async def effect(ctx):
        await ctx.deal_damage()
        n = count_attached(ctx)
        if n == 1 or n >= 3:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.ASLEEP)
        if n >= 2:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
        if n >= 4:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
    return effect


def is_active_pokemon(board, player_id, pokemon=None) -> bool:
    """Poké-Power extra: this Pokémon is in the Active Spot."""
    return pokemon is not None and is_in_active_spot(pokemon)


class PartnerTypedTakesLessPassive(Passive):
    """While a named partner is in play, this Pokémon takes `amount` less
    from attacks by Pokémon of `attacker_types` (after Weakness and
    Resistance). Extra copies of the partner do not stack."""

    def __init__(self, amount, partner_name, attacker_types):
        self.amount = amount
        self.partner_name = partner_name
        self.attacker_types = [getattr(t, "value", t) for t in attacker_types]

    def modify_damage_taken(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return
        if carrier_pokemon(carrier) is not calc.target:
            return
        if not any(
            p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == self.partner_name
            for pid in calc.board.player_ids
            for p in calc.board.pokemon_in_play(pid)
        ):
            return
        if calc.attacker is None:
            return
        types = effective_pokemon_types(calc.board, calc.attacker)
        if not any(t in types for t in self.attacker_types):
            return
        calc.amount = max(0, calc.amount - self.amount)


def partner_typed_takes_less(amount, partner_name, attacker_types) -> Passive:
    """Glowing Screen shape: named partner in play, −N from typed attackers."""
    return PartnerTypedTakesLessPassive(amount, partner_name, attacker_types)


class PartnerRetreatFreePassive(Passive):
    """While a named partner is in play, the carrier's Retreat Cost is 0
    (Volbeat Uplifting Glow). Extra copies of the partner do not matter."""

    def __init__(self, partner_name):
        self.partner_name = partner_name

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier) or carrier
        if pokemon is not holder:
            return cost
        if not any(
            p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == self.partner_name
            for pid in board.player_ids
            for p in board.pokemon_in_play(pid)
        ):
            return cost
        return 0


def partner_retreat_free(partner_name) -> Passive:
    """Uplifting Glow: named partner in play, this Pokémon's Retreat Cost is 0."""
    return PartnerRetreatFreePassive(partner_name)


def may_discard_energy_for_condition(energy_type, *conditions, prompt: str = ""):
    """You may discard 1 Energy providing `energy_type`. If you do, apply
    `conditions` to the Defending Pokémon (Burning Claw / Dark Bind)."""
    type_value = getattr(energy_type, "value", energy_type)

    def pred(card) -> bool:
        return energy_provides_type(card, type_value)

    async def effect(ctx):
        await ctx.deal_damage()
        energies = [
            e for e in ctx.attached_energies(ctx.attacker) if pred(e)
        ]
        if not energies:
            return
        picks = await ctx.choose_cards(
            energies, 1, minimum=0,
            prompt=prompt or "You may discard a matching Energy card",
        )
        if not picks:
            return
        await ctx.discard_cards(picks)
        for condition in conditions:
            await ctx.apply_special_condition(ctx.defender, condition)
    return effect


def may_discard_all_energy_for_damage(energy_type, boosted: int,
                                      prompt: str = ""):
    """You may discard all Energy cards providing `energy_type`. If you do,
    this attack's base damage is `boosted` instead of the printed damage
    (Lightning Strike)."""
    type_value = getattr(energy_type, "value", energy_type)

    def pred(card) -> bool:
        return energy_provides_type(card, type_value)

    async def effect(ctx):
        base_val = getattr(ctx.ability, "damage", 0) or 0
        energies = [
            e for e in ctx.attached_energies(ctx.attacker) if pred(e)
        ]
        if energies and await ctx.ask_yes_no(
            prompt or "Discard all matching Energy cards attached to this Pokémon?"
        ):
            await ctx.discard_energy_from(ctx.attacker, 99, predicate=pred)
            await ctx.deal_damage(boosted)
        elif base_val > 0:
            await ctx.deal_damage(base_val)
    return effect


def flip_return_defender_energy():
    """Poké-Power: flip a coin. If heads, return 1 Energy card attached to
    the Defending Pokémon to the opponent's hand (Fan Away)."""
    async def effect(ctx):
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if not results or not results[0]:
            return
        defender = ctx.defender or ctx.opponent_active()
        if defender is None:
            return
        energies = list(ctx.attached_energies(defender))
        if not energies:
            return
        picks = await ctx.choose_cards(
            energies, 1,
            prompt="Choose an Energy card to return to your opponent's hand",
        )
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
    return effect


def flip_apply_condition(*conditions):
    """Poké-Power: flip a coin; heads applies `conditions` to the Defending
    Pokémon (Chaos Flash)."""
    async def effect(ctx):
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if not results or not results[0]:
            return
        target = ctx.defender or ctx.opponent_active()
        if target is None:
            return
        for condition in conditions:
            await ctx.apply_special_condition(target, condition)
    return effect


def shuffle_random_from_opponent_hand(count: int = 1):
    """Choose `count` cards from the opponent's hand without looking, look
    at them, then shuffle them into the opponent's deck (Surprise)."""
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if ctx.is_attack_effect() and printed > 0:
            await ctx.deal_damage()
        hand = ctx.hand(ctx.opponent_id)
        if not hand:
            return
        picks = random.sample(hand, min(count, len(hand)))
        await ctx.reveal_cards(picks, to_player=ctx.player_id)
        await ctx.shuffle_into_deck(picks, ctx.opponent_id)
    return effect


def flip_knock_out_defender(coins: int = 2):
    """Flip `coins`. If all are heads, the Defending Pokémon is Knocked Out
    (Judgement)."""
    async def effect(ctx):
        results = await ctx.flip_coins(
            coins, ctx.ability.title if ctx.ability else "")
        if results and all(results) and ctx.defender is not None:
            await ctx.knock_out(ctx.defender)
    return effect


def flip_attach_from_discard(predicate=None, prompt: str = ""):
    """Printed damage; flip a coin. If heads, attach 1 matching Energy from
    discard to this Pokémon (Plasma)."""
    pred = is_energy_card if predicate is None else predicate

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if ctx.is_attack_effect() and printed > 0:
            await ctx.deal_damage()
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if not results or not results[0]:
            return
        cards = [c for c in ctx.discard_pile() if pred(c)]
        if not cards:
            return
        picks = await ctx.choose_cards(
            cards, 1, minimum=1,
            prompt=prompt or "Choose an Energy card to attach.",
        )
        if not picks:
            return
        holder = ctx.attacker or ctx.source
        if holder is None:
            return
        if holder.entity_id not in ctx.visual_targets:
            ctx.visual_targets.append(holder.entity_id)
        await ctx.attach_energy(picks[0], holder)
    return effect


def baby_evolution_condition(into_name: str):
    """Poké-Power: a card named `into_name` is in hand (Baby Evolution)."""
    pred = _named(into_name)

    def extra(board, player_id, pokemon=None):
        hand = board.find_player_area(player_id, "hand")
        return any(pred(c) for c in (hand.children if hand else []))
    return poke_power_condition(extra)


def baby_evolution(into_name: str):
    """Put a named Pokémon from hand onto this Pokémon (counts as evolving)
    and remove all damage counters (Baby Evolution)."""
    pred = _named(into_name)

    async def effect(ctx):
        matches = [c for c in ctx.hand() if pred(c)]
        if not matches:
            return
        picks = await ctx.choose_cards(
            matches, 1, minimum=1,
            prompt=f"Choose a {into_name} to put onto this Pokémon",
        )
        if not picks:
            return
        evolved = picks[0]
        await ctx.evolve_pokemon(ctx.source, evolved)
        missing = ctx.max_hp(evolved) - evolved.get_attribute(AttrID.HP, 0)
        if missing > 0:
            await ctx.heal(missing, evolved)
    return effect


def search_basic_or_evo_per_energy():
    """Search the deck for a Basic Pokémon or Evolution card for each Energy
    attached to this Pokémon, show them, put into hand, and shuffle
    (Alluring Smile)."""
    count_attached = count_energy("self")

    async def effect(ctx):
        n = count_attached(ctx)
        picks = await ctx.search_deck(
            lambda c: is_basic_pokemon(c) or is_evolution_pokemon(c),
            count=n, minimum=0,
            prompt="Choose a Basic Pokémon or Evolution card for each Energy attached.",
        ) if n > 0 else []
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def feint_attack(amount: int):
    """Choose 1 of the opponent's Pokémon. Deal `amount` that isn't affected
    by Weakness, Resistance, Poké-Powers, Poké-Bodies, or other effects on
    that Pokémon (Feint Attack)."""
    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, f"Choose a Pokémon to take {amount} damage")
        if target is None:
            target = candidates[0]
        await ctx.deal_damage(
            amount, target=target,
            apply_modifiers=False, ignore_target_effects=True)
    return effect


def rapid_spin():
    """Printed damage; the opponent switches their Active (they choose), then
    you switch this Pokémon with 1 of yours (EX Baltoy Rapid Spin)."""
    async def effect(ctx):
        await ctx.deal_damage()
        await opponent_switches(ctx)
        await ctx.flush_choreography()
        bench = ctx.my_bench()
        if not bench:
            return
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)
    return effect


def lure_condition(*conditions):
    """You may switch the Defending Pokémon with 1 of the opponent's Benched
    Pokémon (you choose), then apply Special Conditions to the Defending
    Pokémon (Cradily Lure Poison)."""
    async def effect(ctx):
        old_active = ctx.opponent_active()
        if old_active is not None and ctx.opponent_bench() \
                and not ctx.effects_blocked(old_active) \
                and await ctx.ask_yes_no(
                    "Switch the Defending Pokémon with 1 of your opponent's "
                    "Benched Pokémon?"):
            target = await ctx.choose_pokemon(
                ctx.opponent_bench(),
                "Choose the opponent's new Active Pokémon",
            )
            if target is not None:
                await ctx.switch_active(ctx.opponent_id, target)
        defender = ctx.opponent_active()
        if defender is not None:
            for condition in conditions:
                await ctx.apply_special_condition(defender, condition)
    return effect


class ExFossilPassive(FossilBodyPassive):
    """EX-era fossils: can't retreat, immune to Special Conditions, and a
    Knock Out doesn't take Prize cards."""

    def __init__(self):
        super().__init__(blocks_conditions=True)

    def modify_prizes_for_knockout(self, pokemon, ctx, count, carrier):
        if pokemon is carrier:
            return 0
        return count


_TOOL_TYPES = (TrainerType.POKEMON_TOOL.value, TrainerType.POKEMON_TOOL_F.value)


def _is_pokemon_tool_card(card) -> bool:
    return card.get_attribute(AttrID.TRAINER_TYPE) in _TOOL_TYPES


def condition_on_damaged(condition, while_active: bool = True):
    """Poké-Body: if this Pokémon is damaged by an opponent's attack
    (even if Knocked Out), the Attacking Pokémon gets `condition`
    (Fire Veil / Poison Payback). Pair with ON_DAMAGED_BY_ATTACK."""
    async def effect(ctx):
        pokemon = ctx.source
        if while_active and not is_in_active_spot(pokemon):
            return
        attacker = ctx.damaged_by
        if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
            return
        await ctx.apply_special_condition(attacker, condition)
    return effect


class TrainerPlayLockPassive(Passive):
    """Matching Trainer cards can't be played from hand.

    opponents_only locks the opponent (Primal Lock); both players when
    False (Primal Veil). while_active gates on the carrier being Active.
    """

    def __init__(self, predicate, opponents_only: bool = True,
                 while_active: bool = False):
        self.predicate = predicate
        self.opponents_only = opponents_only
        self.while_active = while_active

    def blocks_trainer_play(self, card, player_id, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if self.while_active and not is_in_active_spot(holder):
            return False
        if self.opponents_only and player_id == carrier.owning_player_id:
            return False
        return bool(self.predicate(card))


def opponent_cant_play_tools() -> Passive:
    """Primal Lock: as long as this Pokémon is in play, the opponent can't
    play Pokémon Tool cards."""
    return TrainerPlayLockPassive(_is_pokemon_tool_card)


def both_players_cant_play_supporters(while_active: bool = True) -> Passive:
    """Primal Veil: as long as this Pokémon is Active, each player can't
    play Supporter cards."""
    return TrainerPlayLockPassive(
        is_supporter_card, opponents_only=False, while_active=while_active)


async def discard_opponent_tools(ctx):
    """Discard every Pokémon Tool attached to the opponent's Pokémon
    (Primal Lock's come-into-play strip)."""
    tools = [
        child
        for pokemon in ctx.opponent_pokemon_in_play()
        for child in pokemon.children
        if _is_pokemon_tool_card(child)
    ]
    if tools:
        await ctx.discard_cards(tools)


def attach_as_many_from_hand(predicate, target: str = "active", prompt: str = ""):
    """Attach as many matching Energy from hand as you like (Drizzle).

    target 'active' attaches every chosen card to your Active Pokémon;
    'choice' picks a Pokémon per card.
    """
    async def effect(ctx):
        energies = [c for c in ctx.hand() if predicate(c)]
        if not energies:
            return
        picks = await ctx.choose_cards(
            energies, len(energies), minimum=0,
            prompt=prompt or "Choose Energy cards to attach.",
        )
        if not picks:
            return
        if target == "active":
            receiver = ctx.my_active()
            if receiver is None:
                return
            if receiver.entity_id not in ctx.visual_targets:
                ctx.visual_targets.append(receiver.entity_id)
            for card in picks:
                await ctx.attach_energy(
                    card, receiver, counts_as_attachment=True)
            return
        candidates = ctx.my_pokemon_in_play()
        if not candidates:
            return
        for card in picks:
            receiver = await ctx.choose_pokemon(
                candidates, "Choose a Pokémon to attach the Energy to")
            if receiver is None:
                receiver = candidates[0]
            await ctx.attach_energy(card, receiver, counts_as_attachment=True)
    return effect


def search_to_bench_named(*names, count: int = 99, include_basic: bool = False,
                          prompt: str = ""):
    """Search the deck for named Pokémon (and optionally any Basic) and put
    them onto the Bench (Team Assembly / Influence). Stage 1 fossil Pokémon
    enter play without evolving, as the attack's 'treat as Basic' clause."""
    name_set = frozenset(names)

    def pred(card) -> bool:
        name = getattr(def_for(card.archetype_id), "display_name", None)
        if name in name_set:
            return True
        return include_basic and is_basic_pokemon(card)

    return search_to_bench(
        pred, count=count,
        prompt=prompt or "Choose Pokémon to put onto your Bench.",
    )


class EnergyVariationPassive(Passive):
    """This Pokémon's type is every type of basic Energy card attached to it
    (Kecleon Energy Variation). Printed types remain if none are attached."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if pokemon is not carrier:
            return types
        energy_types = []
        for child in carrier.children:
            if not is_basic_energy_card(child):
                continue
            for energy_type in child.get_attribute(AttrID.POKEMON_TYPES) or []:
                if energy_type not in energy_types:
                    energy_types.append(energy_type)
        return energy_types or types


def energy_variation_passive() -> Passive:
    """Poké-Body: this Pokémon is the same type as every attached basic Energy."""
    return EnergyVariationPassive()


def link_blast(match_damage: int, mismatch_damage: int):
    """If this Pokémon and the Defending Pokémon have the same amount of
    Energy attached, deal `match_damage`; otherwise `mismatch_damage`."""
    count_self = count_energy("self")
    count_def = count_energy("defender")

    async def effect(ctx):
        amount = match_damage if count_self(ctx) == count_def(ctx) else mismatch_damage
        await ctx.deal_damage(amount)
    return effect


async def time_spiral(ctx):
    """If the opponent has an Evolved Pokémon, choose 1 and flip. Heads:
    shuffle the highest Stage Evolution card into their deck."""
    candidates = [
        p for p in ctx.opponent_pokemon_in_play()
        if devolvable(p) and not ctx.effects_blocked(p)
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Evolved Pokémon",
    )
    if target is None:
        return
    results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
    if not results or not results[0]:
        return
    owner_id = target.owning_player_id
    removed = await ctx.devolve_pokemon(target, steps=1, destination="deck")
    if removed:
        await ctx.shuffle_deck(owner_id)


async def pull_down(ctx):
    """Remove the highest Stage Evolution card from each of the opponent's
    Evolved Pokémon and put those cards into their hand (Omastar Pull Down)."""
    targets = [
        p for p in ctx.opponent_pokemon_in_play()
        if devolvable(p) and not ctx.effects_blocked(p)
    ]
    for target in targets:
        await ctx.devolve_pokemon(target, steps=1, destination="hand")


async def amnesia(ctx):
    """Choose 1 of the Defending Pokémon's attacks. That Pokémon can't use
    that attack during the opponent's next turn."""
    printed = getattr(ctx.ability, "damage", 0) or 0
    if ctx.is_attack_effect() and printed > 0:
        await ctx.deal_damage()
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    entries = [
        e for e in (defender.get_attribute(AttrID.PIE_ABILITIES) or [])
        if isinstance(e, dict) and e.get("abilityType") == "Attack"
        and e.get("abilityID")
    ]
    if not entries:
        return
    idx = 0
    if len(entries) > 1:
        idx = await ctx.choose(
            "Choose an attack that can't be used during your opponent's next turn",
            [e.get("title", {}).get("id", "Attack") for e in entries],
        )
    entry = entries[idx]
    state = ctx.session.turn_state
    state.attack_locks[(defender.entity_id, entry["abilityID"])] = (
        state.turn_number + 1
    )


def is_baby_pokemon(card) -> bool:
    """EX-era Baby Pokémon carry the Baby Evolution Poké-Power."""
    definition = def_for(getattr(card, "archetype_id", None) or "")
    for ability in getattr(definition, "abilities", None) or []:
        if getattr(ability, "title", None) == "Baby Evolution":
            return True
    return False


async def lanettes_net_search(ctx):
    """Search the deck for up to 3 Basic Pokémon of different types
    (excluding Baby Pokémon), show them, put them into hand, and shuffle."""
    deck_cards = list(ctx.deck(ctx.player_id))
    reps = []
    seen_types = []
    for card in deck_cards:
        if not is_basic_pokemon(card) or is_baby_pokemon(card):
            continue
        types = card.get_attribute(AttrID.POKEMON_TYPES) or []
        if not types or types[0] in seen_types:
            continue
        seen_types.append(types[0])
        reps.append(card)
    picks = await ctx.choose_cards(
        reps, 3, minimum=0,
        prompt="Choose up to 3 Basic Pokémon of different types.",
        display_cards=deck_cards,
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


def rain_dish(amount: int = 10):
    """Poké-Body: between turns, heal `amount` from this Pokémon (Rain Dish).
    Pair with ``Triggers.BETWEEN_TURNS``."""
    async def effect(ctx):
        pokemon = ctx.source
        if pokemon is not None:
            await ctx.heal(amount, pokemon)
    return effect


def _has_damaged_active(board, player_id, pokemon=None) -> bool:
    area = board.find_player_area(player_id, "activePokemonArea")
    return any(
        p.get_attribute(AttrID.HP, 0) < effective_max_hp(board, p)
        for p in (area.children if area else [])
    )


healing_wind_condition = poke_power_condition(_has_damaged_active)


def healing_wind(amount: int = 10):
    """Remove `amount` damage from each of your Active Pokémon (Healing Wind)."""
    async def effect(ctx):
        area = ctx.board.find_player_area(ctx.player_id, "activePokemonArea")
        for pokemon in (area.children if area else []):
            await ctx.heal(amount, pokemon)
    return effect


class OverrideTypePassive(Passive):
    """This Pokémon's type is `type_value` (replaces printed types)."""

    def __init__(self, type_value):
        self.type_value = getattr(type_value, "value", type_value)

    def modify_pokemon_types(self, types, pokemon, carrier):
        if pokemon is not carrier:
            return types
        return [self.type_value]


def eclipse_type_change(new_type):
    """Until the end of your turn, this Pokémon's type is `new_type`
    (Lunar Eclipse / Solar Eclipse)."""
    async def effect(ctx):
        pokemon = ctx.source
        if pokemon is None:
            return
        ctx.add_temporary_passive(
            pokemon, OverrideTypePassive(new_type),
            expires_after_turn=ctx.session.turn_state.turn_number,
        )
    return effect


def named_partner_condition(*names, side: str = "any"):
    """Poké-Power: Special Condition block plus a named partner in play."""
    wanted = set(names)

    def extra(board, player_id, pokemon=None):
        pids = [player_id]
        if side in ("any", "both"):
            other = next((p for p in board.player_ids if p != player_id), None)
            if other:
                pids.append(other)
        elif side == "opponent":
            other = next((p for p in board.player_ids if p != player_id), None)
            pids = [other] if other else []
        return any(
            p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) in wanted
            for pid in pids if pid
            for p in board.pokemon_in_play(pid)
        )
    return poke_power_condition(extra)


def draw_if_opponent_evolved(n: int = 3):
    """If the opponent has any Evolved Pokémon in play, draw `n` cards
    (Cosmic Draw)."""
    async def effect(ctx):
        if any(is_evolution_pokemon(p) for p in ctx.opponent_pokemon_in_play()):
            await ctx.draw_cards(n)
    return effect


def optional_gust_then_damage():
    """Before doing damage, you may switch 1 of the opponent's Benched
    Pokémon with the Defending Pokémon, then deal printed damage to the
    (new) Defending Pokémon (Metal Hook)."""
    async def effect(ctx):
        old_active = ctx.opponent_active()
        bench = ctx.opponent_bench()
        if old_active is not None and bench \
                and not ctx.effects_blocked(old_active) \
                and await ctx.ask_yes_no(
                    "Switch 1 of your opponent's Benched Pokémon with the "
                    "Defending Pokémon?"):
            target = await ctx.choose_pokemon(
                bench, "Choose the opponent's new Active Pokémon",
            ) or bench[0]
            await ctx.switch_active(ctx.opponent_id, target)
        await ctx.deal_damage()
    return effect


def _runnable_supporter(card) -> bool:
    if not is_supporter_card(card):
        return False
    effect = TRAINER_EFFECTS_BY_GUID.get((card.archetype_id or "").lower())
    return effect is not None and effect is not unimplemented


async def copy_supporter_from_opponent_hand(ctx):
    """Look at the opponent's hand. You may use a Supporter found there as
    this attack's effect; the card stays in their hand (Supernatural)."""
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    candidates = [c for c in hand if _runnable_supporter(c)]
    if not candidates:
        return
    picks = await ctx.choose_cards(
        candidates, 1, minimum=0,
        prompt="You may use the effect of a Supporter card from your opponent's hand.",
    )
    if not picks:
        return
    effect = TRAINER_EFFECTS_BY_GUID[(picks[0].archetype_id or "").lower()]
    await effect(ctx)


async def scam_supporter(ctx):
    """Look at the opponent's hand. You may shuffle a Supporter you find
    there into their deck; if you do, they draw a card (Scam)."""
    hand = await ctx.reveal_hand(of_player=ctx.opponent_id)
    supporters = [c for c in hand if is_supporter_card(c)]
    if not supporters:
        return
    if not await ctx.ask_yes_no(
        "Shuffle a Supporter card from your opponent's hand into their deck?"
    ):
        return
    picks = await ctx.choose_cards(
        supporters, 1,
        prompt="Choose a Supporter card to shuffle into your opponent's deck",
    )
    if not picks:
        return
    await ctx.shuffle_into_deck(picks, player_id=ctx.opponent_id)
    await ctx.draw_cards(1, player_id=ctx.opponent_id)


def flip_damage_paralyze_on_heads(coins: int = 2, per_heads: Optional[int] = None):
    """Flip `coins`; deal per_heads (or printed) times heads. If any coin
    is heads, the Defending Pokémon is Paralyzed (Double Bubble)."""
    async def effect(ctx):
        results = await ctx.flip_coins(
            coins, ctx.ability.title if ctx.ability else "")
        heads = sum(1 for r in results if r)
        per = per_heads if per_heads is not None else (
            getattr(ctx.ability, "damage", 0) or 0)
        if heads:
            await ctx.deal_damage(per * heads)
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.PARALYZED)
    return effect


def split_blast(full: int = 100, split: int = 50):
    """Deal `full` to the Defending Pokémon, then discard 1 Energy. If the
    opponent has more than 1 Defending Pokémon, you may deal `split` to
    each of them instead (Typhlosion ex Split Blast)."""
    async def effect(ctx):
        defending = [
            p for p in ctx.opponent_pokemon_in_play()
            if is_in_active_spot(p)
        ]
        if len(defending) > 1 and await ctx.ask_yes_no(
            f"Do {split} damage to each Defending Pokémon instead?"
        ):
            for target in defending:
                await ctx.deal_damage(split, target=target)
        else:
            await ctx.deal_damage(full)
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            prompt="Discard 1 Energy card attached to this Pokémon",
        )
    return effect


def heal_then_switch(counters: int = 3):
    """If you have no Benched Pokémon, this attack does nothing. Remove
    `counters` damage counters from this Pokémon, then switch it with 1
    of your Benched Pokémon (Wailord ex Super Deep Dive)."""
    async def effect(ctx):
        bench = ctx.my_bench()
        if not bench:
            return
        pokemon = ctx.attacker or ctx.source
        if pokemon is not None:
            await ctx.heal(counters * 10, pokemon)
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)
    return effect


async def wallys_training(ctx):
    """Search the deck for 1 card that evolves from your Active Pokémon,
    put it onto that Pokémon (counts as evolving), then shuffle."""
    active = ctx.my_active()
    logic_name = (
        active.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) if active else None
    )
    if logic_name:
        picks = await ctx.search_deck(
            lambda c, name=logic_name:
                c.get_attribute(AttrID.EVOLUTION_LOGIC_FROM) == name,
            count=1, minimum=0,
            prompt="Choose a card that evolves from your Active Pokémon.",
        )
        if picks:
            await ctx.evolve_pokemon(active, picks[0])
    await ctx.shuffle_deck()


def _logic_name(card) -> str:
    return card.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) or ""


def _display_name(card) -> str:
    """Best-effort printable name for matching card text (e.g. 'Articuno ex')."""
    d = def_for(getattr(card, "archetype_id", None) or "")
    if d is not None and getattr(d, "display_name", None):
        return d.display_name
    raw = (card.get_attribute(AttrID.DISPLAY_NAME)
           or card.get_attribute(AttrID.CARD_NAME)
           or card.get_attribute(AttrID.NAME))
    if isinstance(raw, dict):
        return raw.get("id") or raw.get("en") or _logic_name(card)
    return raw or _logic_name(card)


class FrenzyVsNamedPassive(Passive):
    """Poké-Body: this Pokémon's attacks do `bonus` more damage while the
    opponent has any of `names` in play (Frenzy). Names match display_name."""

    def __init__(self, names, bonus: int = 40):
        self.names = tuple(names)
        self.bonus = bonus

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and not calc.is_opposing):
            return
        poke = carrier_pokemon(carrier)
        if poke is None or poke is not calc.attacker:
            return
        mine = calc.attacker.owning_player_id
        opp_id = next((p for p in calc.board.player_ids if p != mine), None)
        if opp_id is None:
            return
        names = set(self.names)
        for p in calc.board.pokemon_in_play(opp_id):
            if _display_name(p) in names:
                calc.amount = calc.amount + self.bonus
                return


def frenzy_vs_named(*names, bonus: int = 40) -> Passive:
    return FrenzyVsNamedPassive(names, bonus=bonus)


class SynchronizedLiftPassive(Passive):
    """Poké-Body: Retreat Cost is 0 while all `required_names` are in play
    on your side (Synchronized Lift)."""

    def __init__(self, *required_names):
        self.required = tuple(required_names)

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        poke = carrier_pokemon(carrier) or carrier
        if pokemon is not poke:
            return cost
        present = {_display_name(p) for p in board.pokemon_in_play(
            pokemon.owning_player_id)}
        if all(n in present for n in self.required):
            return 0
        return cost


def synchronized_lift_passive(*required_names) -> Passive:
    return SynchronizedLiftPassive(*required_names)


def may_move_own_energy(energy_type=None):
    """Deal printed damage, then you may move 1 matching Energy from this
    Pokémon to another of your Pokémon (Ice/Flame/Thunder Gift)."""
    type_value = (getattr(energy_type, "value", energy_type)
                  if energy_type is not None else None)

    async def effect(ctx):
        await ctx.deal_damage(None)
        attacker = ctx.attacker
        if attacker is None:
            return
        others = [p for p in ctx.my_pokemon_in_play() if p is not attacker]
        if not others:
            return
        pred = ((lambda c: energy_provides_type(c, type_value))
                if type_value is not None else is_energy_card)
        energies = [c for c in attacker.children if pred(c)]
        if not energies:
            return
        pick = await ctx.choose_cards(
            energies, 1, minimum=0,
            prompt="You may move an Energy to another of your Pokémon.",
        )
        if not pick:
            return
        target = await ctx.choose_pokemon(
            others, "Choose a Pokémon to move the Energy to")
        if target is not None:
            await ctx.move_energy(pick[0], target)

    return effect


def discard_self_energy_draw(draw: int = 3):
    """Discard 1 Energy from self, then draw `draw` (The Third Eye)."""
    async def effect(ctx):
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            prompt="Discard an Energy card attached to this Pokémon")
        await ctx.draw_cards(draw)
    return effect


def _is_attached_trainer(card) -> bool:
    """True for Tools/TMs attached to a Pokémon (not Energy)."""
    if is_energy_card(card):
        return False
    tt = card.get_attribute(AttrID.TRAINER_TYPE)
    if tt is not None:
        return True
    st = subtypes_for(getattr(card, "archetype_id", None) or "") or []
    return any(s in st for s in (
        "Pokémon Tool", "Pokemon Tool", "Tool", "Technical Machine", "TM"))


def plunder_trainers(damage: Optional[int] = None):
    """Before damage, discard all Trainer cards attached to the Defending
    Pokémon (Plunder)."""
    async def effect(ctx):
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            tools = [c for c in list(defender.children)
                     if _is_attached_trainer(c)]
            if tools:
                await ctx.discard_cards(tools)
        await ctx.deal_damage(damage)
    return effect


def flip_heal_self(amount: int = 10):
    """Deal printed damage; on heads, heal `amount` from self."""
    async def effect(ctx):
        await ctx.deal_damage(None)
        results = await ctx.flip_coins(1, "Sporadic Sponging")
        if results and results[0] and ctx.attacker is not None:
            await ctx.heal(amount, ctx.attacker)
    return effect


def metal_charge(self_counters: int = 1):
    """Deal printed damage, then put damage counters on self."""
    async def effect(ctx):
        await ctx.deal_damage(None)
        if ctx.attacker is not None:
            await ctx.deal_damage(
                self_counters * 10, target=ctx.attacker, apply_modifiers=False)
    return effect


def hypno_wave(bonus: int = 20,
               tails_condition=SpecialConditions.ASLEEP):
    """Flip: heads = printed+bonus; tails = printed + condition."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Hypno Wave")
        heads = bool(results and results[0])
        printed = (ctx.ability.damage if ctx.ability and ctx.ability.damage
                   else 30)
        await ctx.deal_damage(printed + (bonus if heads else 0))
        if not heads and ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, tails_condition)
    return effect


def twister_attack(damage: Optional[int] = None):
    """Flip 2 coins. Both tails → nothing. Else deal damage; discard 1 Energy
    from defender per heads."""
    async def effect(ctx):
        results = await ctx.flip_coins(2, "Twister")
        heads = sum(1 for r in results if r)
        if heads == 0:
            return
        await ctx.deal_damage(damage)
        defender = ctx.defender
        if defender is not None and not ctx.effects_blocked(defender):
            await ctx.discard_energy_from(
                defender, heads,
                prompt="Discard Energy from the Defending Pokémon")
    return effect


async def devolution_beam(ctx):
    """Flip. If heads, choose 1 Evolved Pokémon (either side) and devolve
    the highest stage into that player's hand."""
    results = await ctx.flip_coins(1, "Devolution Beam")
    if not (results and results[0]):
        return
    candidates = [
        p for p in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
        if devolvable(p)
    ]
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose an Evolved Pokémon to devolve")
    if target is not None:
        await ctx.devolve_pokemon(target, steps=1, destination="hand")


def pure_body_on_attach(energy_type=PokemonTypes.WATER):
    """Poké-Body: when attaching Water Energy from hand, discard an Energy
    from this Pokémon (Pure Body). Pair with Triggers.ON_ENERGY_ATTACHED."""
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        if ctx.attaching_player_id != ctx.player_id \
                or ctx.energy_receiver is not ctx.source:
            return
        energy = ctx.attached_energy
        if energy is None or not energy_provides_type(energy, type_value):
            return
        # Must discard one Energy (can be the one just attached if alone)
        await ctx.discard_energy_from(
            ctx.source, 1,
            prompt="Pure Body: discard an Energy card attached to Suicune")
    return effect


def burning_aura(counters: int = 1):
    """Between turns while Active: put counters on each Active Pokémon.
    Pair with Triggers.BETWEEN_TURNS."""
    async def effect(ctx):
        source = ctx.source
        if source is None or not is_in_active_spot(source):
            return
        for pid in ctx.board.player_ids:
            area = ctx.board.find_player_area(pid, "activePokemonArea")
            for pokemon in (area.children if area else []):
                await ctx.deal_damage(
                    counters * 10, target=pokemon, apply_modifiers=False)
    return effect


async def championship_arena_end_turn(ctx):
    """At end of each player's turn, if hand >= 8, discard down to 7.
    Pair Stadium with Triggers.END_OF_TURN; ctx.player_id is the ending player."""
    pid = ctx.player_id
    hand = list(ctx.hand(pid))
    if len(hand) < 8:
        return
    need = len(hand) - 7
    picks = await ctx.choose_cards(
        hand, need, minimum=need,
        prompt=f"Championship Arena: discard {need} card(s)",
        player_id=pid,
    )
    if picks:
        await ctx.discard_cards(picks)


async def tropical_wind(ctx):
    """Flip: heads remove up to 2 damage counters from each Active; tails
    each Active is Asleep."""
    results = await ctx.flip_coins(1, "Tropical Wind")
    actives = []
    for pid in ctx.board.player_ids:
        area = ctx.board.find_player_area(pid, "activePokemonArea")
        actives.extend(area.children if area else [])
    if results and results[0]:
        for a in actives:
            await ctx.heal(20, a)
    else:
        for a in actives:
            await ctx.apply_special_condition(a, SpecialConditions.ASLEEP)


async def tropical_tidal_wave(ctx):
    """Flip: heads discard all opponent's in-play Trainers; tails discard
    all your in-play Trainers excluding Supporters."""
    results = await ctx.flip_coins(1, "Tropical Tidal Wave")
    heads = bool(results and results[0])
    pid = ctx.opponent_id if heads else ctx.player_id
    exclude_supporter = not heads
    to_discard = []
    stadium = ctx.stadium_in_play()
    if stadium is not None and stadium.owning_player_id == pid:
        if not (exclude_supporter and is_supporter_card(stadium)):
            to_discard.append(stadium)
    for p in ctx.board.pokemon_in_play(pid):
        for c in list(p.children):
            if _is_attached_trainer(c):
                if exclude_supporter and is_supporter_card(c):
                    continue
                to_discard.append(c)
    if to_discard:
        await ctx.discard_cards(to_discard)


def healing_sound(heal: int = 30):
    """Heal your Active; Defending is Asleep (Healing Sound)."""
    async def effect(ctx):
        active = ctx.my_active()
        if active is not None:
            await ctx.heal(heal, active)
        if ctx.defender is not None:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.ASLEEP)
    return effect


def flip_or_nothing_paralyze(damage: Optional[int] = None):
    """Flip: heads deal damage + Paralyze; tails do nothing (Dragonbreath)."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Dragonbreath")
        if not (results and results[0]):
            return
        await ctx.deal_damage(damage)
        if ctx.defender is not None:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.PARALYZED)
    return effect


def mill_top_on_heads(count: int = 1):
    """Deal printed damage; on heads opponent discards top `count` of deck."""
    async def effect(ctx):
        await ctx.deal_damage(None)
        results = await ctx.flip_coins(1, "Mix-Up")
        if results and results[0]:
            await ctx.discard_cards(
                ctx.deck_top(count, player_id=ctx.opponent_id))
    return effect


def snipe_own_bench(amount: int = 10):
    """Deal printed damage; also `amount` to 1 of your Benched Pokémon."""
    async def effect(ctx):
        await ctx.deal_damage(None)
        bench = ctx.my_bench()
        if not bench:
            return
        target = await ctx.choose_pokemon(
            bench, "Choose 1 of your Benched Pokémon")
        if target is not None:
            await ctx.deal_damage(amount, target=target, apply_modifiers=False)
    return effect


def damage_then(also):
    """Deal printed damage, then run `also(ctx)`."""
    async def effect(ctx):
        await ctx.deal_damage(None)
        await also(ctx)
    return effect


def damage_each_active(amount: int):
    """Deal `amount` to each Active Pokémon (Big Explosion)."""
    async def effect(ctx):
        for poke in (ctx.my_active(), ctx.opponent_active()):
            if poke is not None:
                await ctx.deal_damage(amount, target=poke)
    return effect


def rainbow_burn(base: int = 30, per: int = 10):
    """`base` + `per` for each type of basic Energy attached (Rainbow Burn)."""
    async def effect(ctx):
        types = set()
        for e in ctx.attached_energies(ctx.attacker) if ctx.attacker else []:
            if not is_basic_energy_card(e):
                continue
            for tv in (e.get_attribute(AttrID.POKEMON_TYPES) or []):
                types.add(tv)
        await ctx.deal_damage(base + per * len(types))
    return effect


def prize_lead_bonus(bonus: int = 20, base: Optional[int] = None):
    """Printed (or `base`) + `bonus` if you have more Prize cards left."""
    async def effect(ctx):
        printed = base if base is not None else (
            ctx.ability.damage if ctx.ability and ctx.ability.damage else 0)
        mine = count_prizes_remaining("mine")(ctx)
        theirs = count_prizes_remaining("opponent")(ctx)
        await ctx.deal_damage(printed + (bonus if mine > theirs else 0))
    return effect


def discard_opponent_hand_down_to(n: int = 5):
    """If opponent hand >= n+1, randomly discard down to `n` (Bad News)."""
    async def effect(ctx):
        hand = list(ctx.hand(ctx.opponent_id))
        if len(hand) <= n:
            return
        need = len(hand) - n
        # Without looking: random picks
        picks = random.sample(hand, need)
        await ctx.discard_cards(picks)
    return effect


def heal_my_active(amount: int = 10):
    """Remove damage from your Active (Healing Wave)."""
    async def effect(ctx):
        active = ctx.my_active()
        if active is not None:
            await ctx.heal(amount, active)
    return effect


def fury_cutter(base: int = 10, per_heads: int = 10, all_heads_bonus: int = 60,
                coins: int = 4):
    """Flip `coins`. All heads → base+all_heads_bonus; else base+per_heads*heads."""
    async def effect(ctx):
        results = await ctx.flip_coins(coins, "Fury Cutter")
        heads = sum(1 for r in results if r)
        if heads == coins:
            await ctx.deal_damage(base + all_heads_bonus)
        else:
            await ctx.deal_damage(base + per_heads * heads)
    return effect


def discard_energy_then_condition(energy_type, *conditions):
    """Discard 1 matching Energy from self, then apply conditions (Poison Spurt)."""
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            predicate=lambda c: energy_provides_type(c, type_value),
            prompt="Discard an Energy card attached to this Pokémon")
        for cond in conditions:
            if ctx.defender is not None:
                await ctx.apply_special_condition(ctx.defender, cond)
    return effect


def kindle_discard_both(energy_type=None):
    """Discard 1 Energy (typed) from self, then 1 Energy from defender (Kindle)."""
    type_value = getattr(energy_type, "value", energy_type) if energy_type else None
    pred = ((lambda c: energy_provides_type(c, type_value))
            if type_value is not None else None)

    async def effect(ctx):
        await ctx.deal_damage(None)
        await ctx.discard_energy_from(
            ctx.attacker, 1, predicate=pred,
            prompt="Discard an Energy card attached to this Pokémon")
        if ctx.defender is not None and not ctx.effects_blocked(ctx.defender):
            await ctx.discard_energy_from(
                ctx.defender, 1,
                prompt="Discard an Energy card from the Defending Pokémon")
    return effect


def may_discard_energy_bonus(bonus: int = 20, base: Optional[int] = None):
    """You may discard 1 Energy from self; if you do, deal base+bonus (Dragon Flame)."""
    async def effect(ctx):
        printed = base if base is not None else (
            ctx.ability.damage if ctx.ability and ctx.ability.damage else 0)
        energies = list(ctx.attached_energies(ctx.attacker) if ctx.attacker else [])
        bonus_amt = 0
        if energies:
            picks = await ctx.choose_cards(
                energies, 1, minimum=0,
                prompt="You may discard an Energy card attached to this Pokémon")
            if picks:
                await ctx.discard_cards(picks)
                bonus_amt = bonus
        await ctx.deal_damage(printed + bonus_amt)
    return effect


def burn_flip_tails_discard_energy(energy_type=None):
    """Defending is Burned; flip — tails discard Energy from self (Scorching Smoke)."""
    type_value = getattr(energy_type, "value", energy_type) if energy_type else None
    pred = ((lambda c: energy_provides_type(c, type_value))
            if type_value is not None else None)

    async def effect(ctx):
        await ctx.deal_damage(None)
        if ctx.defender is not None:
            await ctx.apply_special_condition(ctx.defender, SpecialConditions.BURNED)
        results = await ctx.flip_coins(1, "Scorching Smoke")
        if results and not results[0] and ctx.attacker is not None:
            await ctx.discard_energy_from(
                ctx.attacker, 1, predicate=pred,
                prompt="Discard an Energy card attached to this Pokémon")
    return effect


def discard_typed_energies_then_damage(*energy_types, damage: Optional[int] = None):
    """Discard one of each typed Energy from self, then deal damage (Mist Ball / Dragon Wave)."""
    type_values = [getattr(t, "value", t) for t in energy_types]

    async def effect(ctx):
        for tv in type_values:
            await ctx.discard_energy_from(
                ctx.attacker, 1,
                predicate=lambda c, tv=tv: energy_provides_type(c, tv),
                prompt="Discard the required Energy")
        await ctx.deal_damage(damage)
    return effect


def gigavolt(base: int = 40, bonus: int = 30):
    """Flip: heads deal base+bonus; tails deal base + Paralyze (Gigavolt)."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Gigavolt")
        heads = bool(results and results[0])
        await ctx.deal_damage(base + (bonus if heads else 0))
        if not heads and ctx.defender is not None:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.PARALYZED)
    return effect


# ---- EX3 Dragon remaining helpers ------------------------------------------

def dragon_dance(bonus: int = 40):
    """During your next turn, your Active Pokémon's attacks do +bonus
    (Altaria Dragon Dance). Player-wide, not tied to this attacker."""
    async def effect(ctx):
        state = ctx.session.turn_state
        start = state.turn_number
        ctx.add_turn_damage_modifier(TurnDamageModifier(
            bonus, ctx.player_id,
            opposing_active_only=True,
            expires_after_turn=start + 2,
            source_predicate=lambda _e: state.turn_number > start,
        ))
    return effect


async def conductivity_on_attach(ctx):
    """Opponent attaches Energy from hand → 1 damage counter on that Pokémon
    (Ampharos ex Conductivity). Dedupes across multiple Ampharos on one attach."""
    if ctx.attaching_player_id == ctx.player_id:
        return
    receiver = ctx.energy_receiver
    if receiver is None:
        return
    energy = ctx.attached_energy
    if energy is not None and getattr(energy, "_conductivity_taxed", False):
        return
    if energy is not None:
        setattr(energy, "_conductivity_taxed", True)
    await ctx.deal_damage(
        10, target=receiver, apply_modifiers=False, as_counters=True)


def flip_attach_n_from_discard(count: int = 2, predicate=None, prompt: str = ""):
    """Flip; heads attach up to `count` matching Energy from discard to self
    (Collect Fire). No printed damage assumed."""
    pred = is_basic_energy_card if predicate is None else predicate

    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if ctx.is_attack_effect() and printed > 0:
            await ctx.deal_damage()
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if not results or not results[0]:
            return
        cards = [c for c in ctx.discard_pile() if pred(c)]
        if not cards:
            return
        take = min(count, len(cards))
        picks = await ctx.choose_cards(
            cards, take, minimum=take,
            prompt=prompt or f"Choose {take} Energy card(s) to attach.",
        )
        holder = ctx.attacker or ctx.source
        if holder is None:
            return
        for card in picks:
            await ctx.attach_energy(card, holder)
    return effect


def may_discard_energy_then_snipe(energy_type, amount: int = 30,
                                 pool: str = "bench"):
    """Deal printed; you may discard typed Energy; if you do, snipe `amount`
    to a Benched (or pool) opposing Pokémon (Flame Pillar)."""
    type_value = getattr(energy_type, "value", energy_type)

    async def effect(ctx):
        await ctx.deal_damage()
        energies = [
            e for e in ctx.attached_energies(ctx.attacker)
            if energy_provides_type(e, type_value)
        ]
        if not energies:
            return
        if not await ctx.ask_yes_no(
                "Discard a matching Energy to do damage to a Benched Pokémon?"):
            return
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            predicate=lambda c: energy_provides_type(c, type_value),
            prompt="Discard an Energy card attached to this Pokémon")
        if pool == "bench":
            candidates = ctx.opponent_bench()
        else:
            candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, f"Choose a Pokémon to take {amount} damage")
        if target is not None:
            await ctx.deal_damage(
                amount, target=target, apply_modifiers=False)
    return effect


def power_pinchers_passive(amount: int = 10) -> Passive:
    """While Active, your Active Pokémon's attacks do +N to Defending
    (Crawdaunt Power Pinchers)."""
    class _P(Passive):
        def modify_damage_dealt(self, calc, carrier):
            if not (calc.is_attack and calc.is_opposing):
                return
            if not is_in_active_spot(carrier):
                return
            atk = calc.attacker
            if atk is None or atk.owning_player_id != carrier.owning_player_id:
                return
            if not is_in_active_spot(atk):
                return
            if not calc.to_active:
                return
            calc.amount += amount
    return _P()


def call_for_power():
    """Move 1 Energy from another of your Pokémon onto this one.
    Pair with Activations.UNLIMITED (Dragonite ex Call for Power)."""
    async def effect(ctx):
        me = ctx.source
        if me is None:
            return
        others = [p for p in ctx.my_pokemon_in_play() if p is not me]
        if not others:
            return
        await ctx.move_energy_freely(
            others, [me], max_count=1,
            prompt="Choose an Energy to move to Dragonite ex")
    return effect


def backspin():
    """Printed damage; you may discard 1 Energy; if you do, switch with Bench
    (Forretress Backspin)."""
    async def effect(ctx):
        await ctx.deal_damage()
        energies = list(ctx.attached_energies(ctx.attacker) if ctx.attacker else [])
        if not energies:
            return
        if not await ctx.ask_yes_no(
                "Discard an Energy to switch this Pokémon with a Benched one?"):
            return
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            prompt="Discard an Energy card attached to this Pokémon")
        bench = ctx.my_bench()
        if not bench:
            return
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        if target is not None:
            await ctx.switch_active(ctx.player_id, target)
    return effect


def same_energy_count(ctx) -> bool:
    return count_energy("self")(ctx) == count_energy("defender")(ctx)


def synchronized_search():
    """If same Energy count as Defending, search deck for any 1 card to hand."""
    async def effect(ctx):
        if not same_energy_count(ctx):
            return
        top = list(ctx.deck())
        if not top:
            return
        picks = await ctx.choose_cards(
            top, 1, minimum=1,
            prompt="Choose a card to put into your hand")
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
            await ctx.shuffle_deck(ctx.player_id)
    return effect


def breaking_impact(per: int = 10):
    """Choose an opposing Pokémon; deal per * its (printed) Colorless retreat
    cost, no W/R (Breaking Impact)."""
    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose a Pokémon for Breaking Impact")
        if target is None:
            return
        cost = int(target.get_attribute(AttrID.RETREAT_COST) or 0)
        if cost > 0:
            await ctx.deal_damage(
                per * cost, target=target, apply_modifiers=False)
    return effect


def mind_trip():
    """Printed damage; if same Energy count, Confuse the Defending Pokémon."""
    async def effect(ctx):
        await ctx.deal_damage()
        if same_energy_count(ctx) and ctx.defender is not None:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.CONFUSED)
    return effect


def dragon_crush(amount: int = 10):
    """Flip; heads: `amount` to each Defending + discard 1 Energy from each."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Dragon Crush")
        if not (results and results[0]):
            return
        defending = [
            p for p in ctx.opponent_pokemon_in_play()
            if is_in_active_spot(p)
        ] or ([ctx.defender] if ctx.defender else [])
        for target in defending:
            if target is None:
                continue
            await ctx.deal_damage(amount, target=target)
            if not ctx.effects_blocked(target):
                await ctx.discard_energy_from(
                    target, 1,
                    prompt="Discard an Energy from the Defending Pokémon")
    return effect


def melting_mountain():
    """Discard top of deck; if basic Energy, attach to this Pokémon."""
    async def effect(ctx):
        top = ctx.deck_top(1)
        if not top:
            return
        card = top[0]
        await ctx.discard_cards([card])
        if is_basic_energy_card(card) and ctx.source is not None:
            # re-fetch from discard
            await ctx.attach_energy(card, ctx.source)
    return effect


def lava_flow(base: int = 40, per: int = 20):
    """You may discard any number of basic Energy; deal base + per * discarded."""
    async def effect(ctx):
        energies = [
            e for e in ctx.attached_energies(ctx.attacker)
            if is_basic_energy_card(e)
        ]
        discarded = 0
        if energies:
            picks = await ctx.choose_cards(
                energies, len(energies), minimum=0,
                prompt="Discard any number of basic Energy cards")
            if picks:
                await ctx.discard_cards(picks)
                discarded = len(picks)
        await ctx.deal_damage(base + per * discarded)
    return effect


def spiral_growth():
    """Flip until tails; for each heads attach a basic Energy from discard."""
    async def effect(ctx):
        heads = 0
        while True:
            results = await ctx.flip_coins(1, "Spiral Growth")
            if not results or not results[0]:
                break
            heads += 1
        if heads <= 0 or ctx.attacker is None:
            return
        pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        take = min(heads, len(pool))
        if take <= 0:
            return
        picks = await ctx.choose_cards(
            pool, take, minimum=take,
            prompt=f"Choose {take} basic Energy card(s) to attach")
        for card in picks:
            await ctx.attach_energy(card, ctx.attacker)
    return effect


def dragon_burst(per: int = 40):
    """Discard all Fire or all Lightning Energy; deal per * count discarded."""
    async def effect(ctx):
        fire = [
            e for e in ctx.attached_energies(ctx.attacker)
            if energy_provides_type(e, PokemonTypes.FIRE.value)
        ]
        lightning = [
            e for e in ctx.attached_energies(ctx.attacker)
            if energy_provides_type(e, PokemonTypes.LIGHTNING.value)
        ]
        choices = []
        if fire:
            choices.append("Fire")
        if lightning:
            choices.append("Lightning")
        if not choices:
            await ctx.deal_damage(0)
            return
        if len(choices) == 1:
            pick = choices[0]
        else:
            idx = await ctx.choose(
                "Discard all Fire or all Lightning Energy?", choices)
            pick = choices[idx]
        bundle = fire if pick == "Fire" else lightning
        await ctx.discard_cards(bundle)
        await ctx.deal_damage(per * len(bundle))
    return effect


def speed_growth(count: int = 2, energy_type=PokemonTypes.GRASS):
    """Attach up to `count` typed Energy from hand to your Pokémon any way."""
    return attach_energy_from_hand(
        predicate=lambda c: (
            is_basic_energy_card(c)
            and energy_provides_type(c, getattr(energy_type, "value", energy_type))
        ),
        count=count,
        prompt=f"Choose up to {count} Energy card(s) to attach",
    )


def damage_curse():
    """Put 1 + (damage counters on self) counters on Defending."""
    async def effect(ctx):
        attacker = ctx.attacker
        if attacker is None:
            return
        dmg = max(0, (ctx.max_hp(attacker) - attacker.get_attribute(AttrID.HP, 0)) // 10)
        total = 1 + dmg
        if ctx.defender is not None:
            await ctx.deal_damage(
                total * 10, target=ctx.defender,
                apply_modifiers=False, as_counters=True)
    return effect


def pick_on_look(down_to: int = 5):
    """If opponent hand > down_to, look and choose cards to shuffle into deck
    until they have down_to left (Skarmory Pick On)."""
    async def effect(ctx):
        hand = list(ctx.hand(ctx.opponent_id))
        if len(hand) <= down_to:
            return
        need = len(hand) - down_to
        # Reveal hand to attacker via choose
        picks = await ctx.choose_cards(
            hand, need, minimum=need,
            prompt=f"Choose {need} card(s) for your opponent to shuffle into their deck")
        if picks:
            await ctx.shuffle_into_deck(picks, ctx.opponent_id)
    return effect


def power_count(base: int = 20, bonus: int = 30):
    """base + bonus if your side has fewer Energy cards than opponent's."""
    async def effect(ctx):
        mine = sum(len(ctx.attached_energies(p)) for p in ctx.my_pokemon_in_play())
        theirs = sum(
            len(ctx.attached_energies(p)) for p in ctx.opponent_pokemon_in_play())
        await ctx.deal_damage(base + (bonus if mine < theirs else 0))
    return effect


def quick_dive(amount: int = 50):
    """Flip; heads choose any opposing Pokémon for `amount` (no W/R)."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Quick Dive")
        if not (results and results[0]):
            return
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, f"Choose a Pokémon to take {amount} damage")
        if target is not None:
            await ctx.deal_damage(
                amount, target=target, apply_modifiers=False)
    return effect


def quick_charge_different_types(count: int = 3):
    """Search deck for up to `count` different types of basic Energy to hand."""
    async def effect(ctx):
        pool = [c for c in ctx.deck() if is_basic_energy_card(c)]
        if not pool:
            await ctx.shuffle_deck(ctx.player_id)
            return
        # Pick greedily with type uniqueness enforced by successive filters
        chosen = []
        used_types = set()
        remaining = list(pool)
        for _ in range(count):
            eligible = []
            for c in remaining:
                types = tuple(c.get_attribute(AttrID.POKEMON_TYPES) or [])
                if types and types[0] not in used_types:
                    eligible.append(c)
            if not eligible:
                break
            picks = await ctx.choose_cards(
                eligible, 1, minimum=0,
                prompt="Choose a basic Energy of a new type (or skip)")
            if not picks:
                break
            card = picks[0]
            chosen.append(card)
            remaining = [c for c in remaining if c is not card]
            t = (card.get_attribute(AttrID.POKEMON_TYPES) or [None])[0]
            used_types.add(t)
        if chosen:
            await ctx.put_in_hand(chosen, reveal=True)
        await ctx.shuffle_deck(ctx.player_id)
    return effect


def flip_spread_all(amount: int = 20):
    """Flip; heads deal `amount` to each opposing Pokémon (no W/R on bench)."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, ctx.ability.title if ctx.ability else "")
        if not (results and results[0]):
            return
        for target in ctx.opponent_pokemon_in_play():
            await ctx.deal_damage(
                amount, target=target,
                apply_modifiers=is_in_active_spot(target))
    return effect


def special_circuit(base: int = 20, bonus: int = 40):
    """Snipe: base, or bonus if target has a Poké-Power or Poké-Body."""
    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose a Pokémon for Special Circuit")
        if target is None:
            return
        entries = target.get_attribute(AttrID.PIE_ABILITIES) or []
        has_pb = any(
            isinstance(e, dict) and e.get("abilityType") in (
                "Poké-Power", "Poké-Body", "Poke-Power", "Poke-Body",
                AbilityTypes.POKE_POWER, AbilityTypes.POKE_BODY,
                getattr(AbilityTypes.POKE_POWER, "value", None),
                getattr(AbilityTypes.POKE_BODY, "value", None),
            )
            for e in entries
        )
        # Also check ability_type ints commonly stored
        if not has_pb:
            for e in entries:
                if not isinstance(e, dict):
                    continue
                at = e.get("abilityType")
                if at in (AbilityTypes.POKE_POWER, AbilityTypes.POKE_BODY):
                    has_pb = True
                    break
                if isinstance(at, str) and ("Power" in at or "Body" in at):
                    has_pb = True
                    break
        amt = bonus if has_pb else base
        await ctx.deal_damage(
            amt, target=target,
            apply_modifiers=is_in_active_spot(target))
    return effect


def extra_circuit(base: int = 20, bonus: int = 40):
    """Snipe: base, or bonus if target is Pokémon-ex."""
    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose a Pokémon for Extra Circuit")
        if target is None:
            return
        amt = bonus if is_pokemon_ex(target) else base
        await ctx.deal_damage(
            amt, target=target,
            apply_modifiers=is_in_active_spot(target))
    return effect


def slimy_water(base: int = 40, per: int = 10):
    """base + per * Defending Pokémon's Colorless retreat cost."""
    async def effect(ctx):
        cost = 0
        if ctx.defender is not None:
            cost = int(ctx.defender.get_attribute(AttrID.RETREAT_COST) or 0)
        await ctx.deal_damage(base + per * cost)
    return effect


def quick_touch():
    """You may switch; if you do, you may move any Grass Energy to new Active."""
    async def effect(ctx):
        await ctx.deal_damage()
        attacker = ctx.attacker
        bench = ctx.my_bench()
        if not bench or attacker is None:
            return
        if not await ctx.ask_yes_no(
                "Switch this Pokémon with 1 of your Benched Pokémon?"):
            return
        target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
        if target is None:
            return
        await ctx.switch_active(ctx.player_id, target)
        # Move Grass Energy from old (now bench) to new active
        grass = [
            e for e in ctx.attached_energies(attacker)
            if energy_provides_type(e, PokemonTypes.GRASS.value)
        ]
        if not grass:
            return
        picks = await ctx.choose_cards(
            grass, len(grass), minimum=0,
            prompt="Move any number of Grass Energy to the new Active")
        for e in picks:
            await ctx.move_energy(e, target)
    return effect


def loose_shell_search():
    """When played to evolve, you may search for Shedinja onto Bench as Basic."""
    async def effect(ctx):
        if not await ctx.ask_yes_no(
                "Search your deck for Shedinja and put it onto your Bench?"):
            return
        await search_to_bench_named(
            "Shedinja", count=1, include_basic=False,
            prompt="Choose Shedinja to put onto your Bench",
        )(ctx)
    return effect


def magnetic_field():
    """Discard 1 from hand; put up to 2 basic Energy from discard into hand
    (can't return the discarded card)."""
    def cond(board, player_id, pokemon=None):
        from spirit.game.card_effects.trainers import is_basic_energy_card as _ibe
        disc = board.discard_pile(player_id) if hasattr(board, 'discard_pile') else []
        # board API via session later — poke_power_condition wraps
        return True

    async def effect(ctx):
        disc_energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        if not disc_energy:
            return
        hand = list(ctx.hand())
        if not hand:
            return
        dump = await ctx.choose_cards(
            hand, 1, minimum=1,
            prompt="Discard a card from your hand")
        if not dump:
            return
        dumped = dump[0]
        await ctx.discard_cards(dump)
        # Refresh discard; exclude the card just discarded from return
        pool = [
            c for c in ctx.discard_pile()
            if is_basic_energy_card(c) and c is not dumped
        ]
        if not pool:
            return
        take = min(2, len(pool))
        picks = await ctx.choose_cards(
            pool, take, minimum=0,
            prompt="Choose up to 2 basic Energy from your discard pile")
        if picks:
            await ctx.put_in_hand(picks, reveal=True)
    return effect


def toxic_gas_passive() -> Passive:
    """While Active, ignore all Poké-Powers and Poké-Bodies other than Toxic Gas."""
    class _P(Passive):
        def blocks_ability(self, pokemon, ability, carrier):
            if not is_in_active_spot(carrier):
                return False
            title = getattr(ability, "title", None)
            if title == "Toxic Gas":
                return False
            at = getattr(ability, "ability_type", None)
            return at in (AbilityTypes.POKE_POWER, AbilityTypes.POKE_BODY)
    return _P()


def wonder_guard_passive() -> Passive:
    """Prevent damage + attack effects from Evolved Pokémon and Pokémon-ex."""
    class _P(Passive):
        def _match(self, attacker, target, carrier):
            if carrier_pokemon(carrier) is not target:
                return False
            if attacker is None:
                return False
            return is_pokemon_ex(attacker) or is_evolution_pokemon(attacker)

        def prevents_damage(self, calc, carrier):
            return bool(
                calc.is_attack and calc.is_opposing
                and self._match(calc.attacker, calc.target, carrier))

        def blocks_attack_effects_from(self, target, carrier, attacker):
            return self._match(attacker, target, carrier)
    return _P()


def submerge_passive() -> Passive:
    """While on the Bench, prevent all damage from opponent's attacks."""
    def pred(calc, carrier):
        holder = carrier_pokemon(carrier) or carrier
        return (
            calc.is_attack and calc.is_opposing
            and calc.target is holder
            and not is_in_active_spot(holder)
        )
    return prevent_damage_when(pred)


def energy_guard_passive(amount: int = 10) -> Passive:
    """Takes `amount` less from attacks while any basic Energy is attached."""
    return takes_less_passive(
        amount,
        protects=lambda target, carrier: (
            carrier_pokemon(carrier) is target
            and any(is_basic_energy_card(c) for c in target.children)
        ),
    )


def levitate_passive() -> Passive:
    """Retreat cost 0 while any basic Energy is attached."""
    return retreat_free_when(
        lambda pokemon, carrier: (
            carrier_pokemon(carrier) is pokemon
            and any(is_basic_energy_card(c) for c in pokemon.children)
        )
    )


def draw_then_discard(draw: int = 3, discard: int = 1):
    """Draw `draw`, then discard `discard` from hand (TV Reporter)."""
    async def effect(ctx):
        await ctx.draw_cards(draw)
        await ctx.discard_from_hand(
            discard, minimum=discard,
            prompt=f"Choose {discard} card(s) to discard")
    return effect


def scoop_own_non_ex():
    """Choose 1 of your non-ex Pokémon; return it and attachments to hand
    (Mr. Briney's Compassion)."""
    async def effect(ctx):
        candidates = [
            p for p in ctx.my_pokemon_in_play() if not is_pokemon_ex(p)
        ]
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, "Choose a Pokémon to return to your hand")
        if target is None:
            return
        was_active = target is ctx.my_active()
        stack = full_stack(target)
        await ctx.put_in_hand(stack, reveal=False)
        if was_active:
            async def _promote():
                if not await ctx.session._promote_new_active(ctx.player_id):
                    screen_name = ctx.session.players[ctx.player_id].screen_name
                    await ctx.session.end_game(
                        ctx.opponent_id, f"{screen_name} has no Pokémon left")
            ctx.deferred_actions.append(_promote)
    return effect


class BalloonBerryPassive(Passive):
    """Approx: holder retreats for free. Full text also discards this tool
    instead of Energy; that discard-on-retreat hook is not wired yet."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        holder = carrier_pokemon(carrier) or carrier
        if holder is pokemon:
            return 0
        return cost


def high_pressure_passive() -> Passive:
    """Each player pays [C] less to retreat Fire and Water Pokémon."""
    return retreat_discount(
        1,
        target_pred=lambda pokemon, carrier: any(
            t in (pokemon.get_attribute(AttrID.POKEMON_TYPES) or [])
            for t in (PokemonTypes.FIRE.value, PokemonTypes.WATER.value)
        ),
    )


def low_pressure_passive(amount: int = 10) -> Passive:
    """Each Grass and Lightning Pokémon gets +amount HP."""
    class _P(Passive):
        def max_hp_bonus(self, pokemon, carrier):
            types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
            if PokemonTypes.GRASS.value in types or PokemonTypes.LIGHTNING.value in types:
                return amount
            return 0
    return _P()


class BufferPiecePassive(Passive):
    """Takes 20 less after W/R. (End-of-opponent-turn discard approximated
    separately if the engine supports tool lifetime; damage reduce is the core.)"""

    def modify_damage_taken(self, calc, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if calc.is_attack and calc.is_opposing and calc.target is holder:
            calc.amount = max(0, calc.amount - 20)

def energy_recycle_system():
    """Show 1 basic Energy from discard to hand, OR show 3 and shuffle into deck."""
    async def effect(ctx):
        pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        if not pool:
            return
        options = ["Put 1 basic Energy into your hand"]
        if len(pool) >= 3:
            options.append("Shuffle 3 basic Energy into your deck")
        idx = await ctx.choose("Energy Recycle System", options)
        if idx == 0 or len(options) == 1:
            picks = await ctx.choose_cards(
                pool, 1, minimum=1,
                prompt="Choose a basic Energy to put into your hand")
            if picks:
                await ctx.put_in_hand(picks, reveal=True)
        else:
            picks = await ctx.choose_cards(
                pool, 3, minimum=3,
                prompt="Choose 3 basic Energy to shuffle into your deck")
            if picks:
                await ctx.shuffle_into_deck(picks, ctx.player_id)
    return effect

def has_team_in_name(*teams: str):
    """True if display_name contains any of the team strings (Team Aqua/Magma)."""
    def pred(card) -> bool:
        name = _display_name(card) or ""
        return any(team in name for team in teams)
    return pred


def defender_has_team(*teams: str):
    pred = has_team_in_name(*teams)
    def cond(ctx) -> bool:
        return ctx.defender is not None and pred(ctx.defender)
    return cond


def second_strike(base: int, bonus: int, counters: int = 2):
    """base + bonus if Defending already has >= counters damage counters."""
    async def effect(ctx):
        dmg = 0
        if ctx.defender is not None:
            dmg = max(0, (ctx.max_hp(ctx.defender) - ctx.defender.get_attribute(AttrID.HP, 0)) // 10)
        await ctx.deal_damage(base + (bonus if dmg >= counters else 0))
    return effect


def bonus_if_damaged(bonus: int, base: Optional[int] = None):
    """Printed (or base) + bonus if Defending already has damage counters."""
    async def effect(ctx):
        printed = base if base is not None else (
            ctx.ability.damage if ctx.ability and ctx.ability.damage else 0)
        dmg = 0
        if ctx.defender is not None:
            dmg = max(0, (ctx.max_hp(ctx.defender) - ctx.defender.get_attribute(AttrID.HP, 0)) // 10)
        await ctx.deal_damage(printed + (bonus if dmg > 0 else 0))
    return effect


def bonus_if_ex(bonus: int, base: Optional[int] = None):
    async def effect(ctx):
        printed = base if base is not None else (
            ctx.ability.damage if ctx.ability and ctx.ability.damage else 0)
        await ctx.deal_damage(printed + (bonus if defender_is_ex(ctx) else 0))
    return effect


def bonus_if_special_condition(bonus: int, base: Optional[int] = None):
    async def effect(ctx):
        printed = base if base is not None else (
            ctx.ability.damage if ctx.ability and ctx.ability.damage else 0)
        from spirit.game.card_effects.attacks_common import defender_has_any_condition
        await ctx.deal_damage(
            printed + (bonus if defender_has_any_condition(ctx) else 0))
    return effect


def force_opponent_switch():
    """Printed damage then opponent switches Defending (Roar / Kick Away)."""
    async def effect(ctx):
        printed = getattr(ctx.ability, "damage", 0) or 0
        if printed > 0:
            await ctx.deal_damage()
        await opponent_switches(ctx)
    return effect


def discard_n_energy_then_damage(n: int = 2, damage: Optional[int] = None):
    """Discard n Energy from self, then deal damage (Bright Flame)."""
    async def effect(ctx):
        await ctx.discard_energy_from(
            ctx.attacker, n,
            prompt=f"Discard {n} Energy card(s) attached to this Pokémon")
        await ctx.deal_damage(damage)
    return effect


def growth_attach(energy_type=PokemonTypes.GRASS):
    """Attach 1 typed Energy from hand to self (Growth)."""
    type_value = getattr(energy_type, "value", energy_type)
    return attach_from_hand(
        lambda c: is_basic_energy_card(c) and energy_provides_type(c, type_value),
        target="active",
        prompt="Choose an Energy card to attach",
    )


def pin_missile(coins: int = 4, per: int = 10):
    from spirit.game.card_effects.attacks_common import flip_damage
    return flip_damage(coins=coins, per_heads=per)


def team_play_damage(team: str = "Team Magma", per: int = 10):
    """per * count of in-play Pokémon with team in name (both sides)."""
    async def effect(ctx):
        pred = has_team_in_name(team)
        n = sum(1 for p in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
                if pred(p))
        await ctx.deal_damage(per * n)
    return effect


def power_blow():
    """10 + 10 per Energy attached to self."""
    return damage_per(count_energy("self"), 10, base=10)



# --- EX4 Team Magma vs Team Aqua -------------------------------------------

def power_saver_condition(team: str, min_count: int = 4):
    """Attack usable only when >= min_count in-play Pokémon have `team` in name."""
    pred = has_team_in_name(team)
    def cond(board, player_id, pokemon=None):
        n = 0
        for pid in board.player_ids:
            for poke in board.pokemon_in_play(pid):
                if pred(poke):
                    n += 1
        return n >= min_count
    return cond


def primal_vibes_passive() -> Passive:
    """While Active, opponent can't evolve from hand (Primal Vibes / Primal Law)."""
    class _P(Passive):
        def blocks_evolution(self, player_id, target, carrier):
            return (
                player_id != carrier.owning_player_id
                and is_in_active_spot(carrier)
            )
    return _P()


def team_hideout_retreat_passive(team: str) -> Passive:
    """Pokémon without `team` in name pay [C] more to retreat."""
    pred = has_team_in_name(team)
    class _P(Passive):
        def modify_retreat_cost(self, cost, pokemon, carrier, board):
            if pred(pokemon):
                return cost
            return cost + 1
    return _P()


async def magma_hideout_watch(ctx):
    """Team Magma Hideout: 1 damage counter on Basic benched from hand
    that does not have Team Magma in its name."""
    pokemon = ctx.benched_pokemon
    if pokemon is None:
        return
    if has_team_in_name("Team Magma")(pokemon):
        return
    # Only Basics (Gapejaw-style; Hideout text is Basic from hand)
    stage = pokemon.get_attribute(AttrID.STAGE)
    if stage not in (None, PokemonStage.BASIC.value):
        return
    await ctx.deal_damage(10, target=pokemon, apply_modifiers=False, as_counters=True)


class StrengthCharmPassive(Passive):
    """Attacks from the holder do +10 to the Active (after W/R).
    Full text discards the Charm at end of that turn; damage boost is the core."""

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier) or carrier
        if (
            calc.is_attack
            and calc.attacker is holder
            and calc.target is not None
            and is_in_active_spot(calc.target)
        ):
            calc.amount += 10


def attach_to_team(*teams: str):
    pred = has_team_in_name(*teams)
    def check(pokemon) -> bool:
        return pred(pokemon)
    return check


def dual_ball():
    """Flip 2 coins; for each heads search a Basic Pokémon into hand."""
    from spirit.game.session.effects import is_basic_pokemon
    async def effect(ctx):
        results = await ctx.flip_coins(2, "Dual Ball")
        heads = sum(1 for r in results if r)
        for _ in range(heads):
            picks = await ctx.search_deck(
                is_basic_pokemon, count=1, minimum=0,
                prompt="Choose a Basic Pokémon to put into your hand.",
            )
            await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def team_ball(team: str):
    """Heads: any Pokémon with team in name; tails: Basic with team in name."""
    from spirit.game.session.effects import is_basic_pokemon
    pred = has_team_in_name(team)
    async def effect(ctx):
        results = await ctx.flip_coins(1, f"{team} Ball")
        heads = bool(results and results[0])
        if heads:
            def match(c):
                return is_pokemon_card(c) and pred(c)
            prompt = f"Choose a Pokémon with {team} in its name"
        else:
            def match(c):
                return is_basic_pokemon(c) and pred(c)
            prompt = f"Choose a Basic Pokémon with {team} in its name"
        picks = await ctx.search_deck(match, count=1, minimum=0, prompt=prompt)
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def team_schemer(team: str):
    """Discard 1 Pokémon from hand; draw 3 (4 if discarded name has team)."""
    from spirit.game.session.effects import is_pokemon_card
    pred = has_team_in_name(team)
    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_pokemon_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=1, prompt="Discard a Pokémon from your hand")
        if not picks:
            return
        bonus = pred(picks[0])
        await ctx.discard_cards(picks)
        await ctx.draw_cards(4 if bonus else 3)
    return effect


def team_conspirator(team: str):
    """Search up to 2 in any combination of Basic team Pokémon and basic Energy."""
    from spirit.game.session.effects import is_basic_pokemon, is_pokemon_card
    pred = has_team_in_name(team)
    def match(c):
        if is_basic_energy_card(c):
            return True
        return is_basic_pokemon(c) and pred(c)
    async def effect(ctx):
        picks = await ctx.search_deck(
            match, count=2, minimum=0,
            prompt=f"Choose up to 2 Basic {team} Pokémon and/or basic Energy",
        )
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def _stage_of_card(card) -> int:
    stage = card.get_attribute(AttrID.STAGE)
    if stage is not None:
        return stage
    definition = def_for(card.archetype_id)
    return getattr(getattr(definition, "stage", None), "value", definition.stage if definition else 0)


def archie_maxie(team: str, from_zones=("deck",)):
    """Search a team Pokémon onto Bench as Basic; Stage 2 gets 2 damage counters.

    Archie: deck. Maxie: hand or discard.
    """
    from spirit.game.session.effects import is_pokemon_card
    pred = has_team_in_name(team)
    async def effect(ctx):
        space = 5 - len(ctx.my_bench())
        if space <= 0:
            return
        pool = []
        if "deck" in from_zones:
            deck = ctx.board.find_player_area(ctx.player_id, "deck")
            pool.extend(c for c in (deck.children if deck else []) if is_pokemon_card(c) and pred(c))
        if "hand" in from_zones:
            pool.extend(c for c in ctx.hand() if is_pokemon_card(c) and pred(c))
        if "discard" in from_zones:
            pool.extend(c for c in ctx.discard_pile() if is_pokemon_card(c) and pred(c))
        # Dedup by entity_id
        seen = set()
        uniq = []
        for c in pool:
            if c.entity_id not in seen:
                seen.add(c.entity_id)
                uniq.append(c)
        if not uniq:
            if "deck" in from_zones:
                await ctx.shuffle_deck()
            return
        picks = await ctx.choose_cards(
            uniq, 1, minimum=1,
            prompt=f"Choose a Pokémon with {team} in its name to Bench",
        )
        if not picks:
            if "deck" in from_zones:
                await ctx.shuffle_deck()
            return
        card = picks[0]
        stage = _stage_of_card(card)
        if not await ctx.bench_pokemon(card):
            if "deck" in from_zones:
                await ctx.shuffle_deck()
            return
        if stage == PokemonStage.STAGE2.value:
            await ctx.deal_damage(20, target=card, apply_modifiers=False, as_counters=True)
        if "deck" in from_zones:
            await ctx.shuffle_deck()
    return effect


def delayed_condition(*conditions, poison_counters: int = 1):
    """At end of opponent's next turn (checkup), apply conditions to Defending
    if it is still the same Active (Slow-Acting Poison / Aqua Trance)."""
    async def effect(ctx):
        target = ctx.defender
        if target is None:
            return
        # Deal printed damage first when present
        printed = getattr(ctx.ability, "damage", 0) or 0
        if printed:
            await ctx.deal_damage()
        owner_id = target.owning_player_id
        target_id = target.entity_id

        def _guard(board):
            active = board.active_pokemon(owner_id) if owner_id else None
            return active is not None and active.entity_id == target_id

        async def _fire(session):
            pokemon = session.board_state.get_entity(target_id)
            if pokemon is None:
                return
            from spirit.game.session.effects import EffectContext
            ectx = EffectContext(session, owner_id, pokemon, None)
            for cond in conditions:
                await ectx.apply_special_condition(
                    pokemon, cond, poison_counters=poison_counters)

        ctx.schedule_at_checkup(1, _fire, guard=_guard)
    return effect


def volcanic_ash(amount: int = 100, energy_count: int = 2,
                 energy_type=PokemonTypes.FIRE):
    """Discard `energy_count` typed Energy, then snipe `amount` (no W/R on bench)."""
    type_value = getattr(energy_type, "value", energy_type)
    async def effect(ctx):
        discarded = await ctx.discard_energy_from(
            ctx.attacker, energy_count,
            predicate=lambda c: is_basic_energy_card(c) and energy_provides_type(c, type_value),
            prompt=f"Discard {energy_count} Fire Energy",
        )
        if len(discarded) < energy_count:
            return
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, f"Choose a Pokémon to take {amount} damage")
        if target is None:
            return
        await ctx.deal_damage(amount, target=target, apply_modifiers=False)
    return effect


def kerzap(base: int = 40, bonus: int = 40, energy_type=PokemonTypes.LIGHTNING):
    """Flip: heads does base+bonus and discard all typed Energy from self."""
    type_value = getattr(energy_type, "value", energy_type)
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Kerzap")
        if results and results[0]:
            await ctx.deal_damage(base + bonus)
            await ctx.discard_energy_from(
                ctx.attacker, 99,
                predicate=lambda c: energy_provides_type(c, type_value),
                prompt="Discard all Lightning Energy",
            )
        else:
            await ctx.deal_damage(base)
    return effect


def green_heal(amount: int = 40, energy_type=PokemonTypes.GRASS):
    """Heal `amount` on each of your Pokémon with typed Energy attached."""
    type_value = getattr(energy_type, "value", energy_type)
    async def effect(ctx):
        for p in ctx.my_pokemon_in_play():
            if any(is_basic_energy_card(c) and energy_provides_type(c, type_value)
                   for c in p.children):
                await ctx.heal(amount, p)
    return effect


def poison_ring():
    """Poison Defending; it can't retreat until end of opponent's next turn."""
    from spirit.game.card_effects.attacks_common import condition_attack
    return condition_attack(SpecialConditions.POISONED, no_retreat=True)


def energy_flip(snipe: int = 10):
    """Snipe bench `snipe`; may move an Energy from that Pokémon to Active."""
    async def effect(ctx):
        bench = ctx.opponent_bench()
        if not bench:
            return
        target = await ctx.choose_pokemon(
            bench, f"Choose a Benched Pokémon to take {snipe} damage")
        if target is None:
            return
        await ctx.deal_damage(snipe, target=target, apply_modifiers=False)
        energies = [c for c in target.children if is_energy_card(c)]
        active = ctx.board.active_pokemon(ctx.opponent_id)
        if energies and active is not None and await ctx.ask_yes_no(
                "Move an Energy from that Pokémon to the Active Pokémon?"):
            picks = await ctx.choose_cards(
                energies, 1, minimum=1, prompt="Choose an Energy to move")
            if picks:
                await ctx.move_energy(picks[0], active)
    return effect


def reverse_stream(base: int = 50, per: int = 10):
    """May return all basic Energy from self to hand; if so, +per per Energy."""
    async def effect(ctx):
        basics = [c for c in ctx.attacker.children if is_basic_energy_card(c)]
        bonus = 0
        if basics and await ctx.ask_yes_no(
                "Return all basic Energy attached to this Pokémon to your hand?"):
            bonus = per * len(basics)
            await ctx.put_in_hand(basics, reveal=False)
        await ctx.deal_damage(base + bonus)
    return effect


def crushing_wave(amount: int = 40):
    """Snipe `amount`; on heads discard Energy from that Pokémon."""
    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, f"Choose a Pokémon to take {amount} damage")
        if target is None:
            return
        await ctx.deal_damage(amount, target=target, apply_modifiers=False)
        results = await ctx.flip_coins(1, "Crushing Wave")
        if results and results[0]:
            await ctx.discard_energy_from(
                target, 1, prompt="Discard an Energy from the Defending Pokémon")
    return effect


def may_discard_energy_paralyze(energy_type=None):
    """You may discard typed Energy; if you do, Paralyze (Dark Bind)."""
    async def effect(ctx):
        await ctx.deal_damage()
        pred = None
        if energy_type is not None:
            tv = getattr(energy_type, "value", energy_type)
            pred = lambda c, tv=tv: energy_provides_type(c, tv)
        energies = [c for c in ctx.attacker.children
                    if is_energy_card(c) and (pred is None or pred(c))]
        if energies and await ctx.ask_yes_no("Discard a Darkness Energy to Paralyze?"):
            discarded = await ctx.discard_energy_from(
                ctx.attacker, 1, predicate=pred,
                prompt="Discard a Darkness Energy")
            if discarded:
                await ctx.apply_special_condition(
                    ctx.defender, SpecialConditions.PARALYZED)
    return effect


def dark_poison():
    """Discard a basic Energy or do nothing; then Poison."""
    async def effect(ctx):
        discarded = await ctx.discard_energy_from(
            ctx.attacker, 1,
            predicate=is_basic_energy_card,
            prompt="Discard a basic Energy or this attack does nothing",
        )
        if not discarded:
            return
        await ctx.deal_damage()
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)
    return effect


def aqua_reverse(team: str = "Team Magma"):
    """Before damage, may switch Defending with benched team Pokémon."""
    pred = has_team_in_name(team)
    async def effect(ctx):
        bench = [p for p in ctx.opponent_bench() if pred(p)]
        if bench and await ctx.ask_yes_no(
                f"Switch the Defending Pokémon with a Benched Pokémon that has {team} in its name?"):
            target = await ctx.choose_pokemon(bench, "Choose the new Active Pokémon")
            if target is not None:
                await ctx.switch_active(ctx.opponent_id, target)
        await ctx.deal_damage()
    return effect


def dark_lift_passive(energy_type=PokemonTypes.DARKNESS) -> Passive:
    """Retreat cost 0 while typed Energy attached."""
    tv = getattr(energy_type, "value", energy_type)
    return retreat_free_when(
        lambda pokemon, carrier: (
            carrier_pokemon(carrier) is pokemon
            and any(energy_provides_type(c, tv) for c in pokemon.children)
        )
    )


def hydro_reverse(base: int = 30, per: int = 10, energy_type=PokemonTypes.WATER):
    """May return any number of typed basic Energy from all your Pokémon; +per each."""
    tv = getattr(energy_type, "value", energy_type)
    async def effect(ctx):
        pool = []
        for p in ctx.my_pokemon_in_play():
            for c in p.children:
                if is_basic_energy_card(c) and energy_provides_type(c, tv):
                    pool.append(c)
        bonus = 0
        if pool and await ctx.ask_yes_no(
                "Return any number of basic Water Energy to your hand?"):
            picks = await ctx.choose_cards(
                pool, len(pool), minimum=0,
                prompt="Choose basic Water Energy to return to your hand")
            if picks:
                bonus = per * len(picks)
                await ctx.put_in_hand(picks, reveal=False)
        await ctx.deal_damage(base + bonus)
    return effect


def land_stream(base: int = 50, per: int = 10):
    """May discard any number of basic Energy from self; +per each."""
    async def effect(ctx):
        pool = [c for c in ctx.attacker.children if is_basic_energy_card(c)]
        bonus = 0
        if pool and await ctx.ask_yes_no(
                "Discard any number of basic Energy attached to this Pokémon?"):
            picks = await ctx.choose_cards(
                pool, len(pool), minimum=0,
                prompt="Choose basic Energy to discard")
            if picks:
                bonus = per * len(picks)
                await ctx.discard_cards(picks)
        await ctx.deal_damage(base + bonus)
    return effect


def dig_under(amount: int = 10):
    """Snipe `amount`; ignore W/R and effects."""
    async def effect(ctx):
        candidates = ctx.opponent_pokemon_in_play()
        if not candidates:
            return
        target = await ctx.choose_pokemon(
            candidates, f"Choose a Pokémon to take {amount} damage")
        if target is None:
            return
        await ctx.deal_damage(
            amount, target=target, apply_modifiers=False, ignore_target_effects=True)
    return effect


def psymist(counters: int = 1, coins: int = 2):
    """Flip coins; for each heads place counters on a chosen opponent Pokémon."""
    async def effect(ctx):
        results = await ctx.flip_coins(coins, "Psymist")
        for _ in range(sum(1 for r in results if r)):
            candidates = ctx.opponent_pokemon_in_play()
            if not candidates:
                break
            target = await ctx.choose_pokemon(
                candidates, f"Place {counters} damage counter(s)")
            if target is None:
                break
            await ctx.deal_damage(
                counters * 10, target=target, apply_modifiers=False, as_counters=True)
    return effect


def pain_amplifier(counters: int = 1):
    """Place counters on each opposing Pokémon that already has damage."""
    async def effect(ctx):
        for p in ctx.opponent_pokemon_in_play():
            hp = p.get_attribute(AttrID.HP, 0)
            max_hp = ctx.max_hp(p)
            if max_hp - hp > 0:
                await ctx.deal_damage(
                    counters * 10, target=p, apply_modifiers=False, as_counters=True)
    return effect


def clay_pulse(amount: int = 10, self_base: int = 20):
    """Printed damage to Active; also `amount` to each damaged benched opponent."""
    async def effect(ctx):
        await ctx.deal_damage()
        for p in ctx.opponent_bench():
            hp = p.get_attribute(AttrID.HP, 0)
            if ctx.max_hp(p) - hp > 0:
                await ctx.deal_damage(amount, target=p, apply_modifiers=False)
    return effect


def magma_spurt(mill: int = 5, per: int = 30, types=(PokemonTypes.FIRE, PokemonTypes.FIGHTING)):
    """Discard top `mill`; per * count of matching basic Energy among them."""
    type_values = {getattr(t, "value", t) for t in types}
    async def effect(ctx):
        cards = ctx.deck_top(mill)
        await ctx.discard_cards(cards)
        n = sum(
            1 for c in cards
            if is_basic_energy_card(c)
            and any(energy_provides_type(c, tv) for tv in type_values)
        )
        await ctx.deal_damage(per * n)
    return effect


def snarl_or_paralyze(heads_damage: int = 10):
    """Heads: damage; tails: Paralyze."""
    async def effect(ctx):
        results = await ctx.flip_coins(1, "Snarl")
        if results and results[0]:
            await ctx.deal_damage(heads_damage)
        else:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.PARALYZED)
    return effect


def may_discard_stadium_then_damage():
    """You may discard any Stadium; then printed damage (Knock Over)."""
    async def effect(ctx):
        if ctx.stadium_in_play() and await ctx.ask_yes_no("Discard the Stadium in play?"):
            await ctx.discard_stadium()
        await ctx.deal_damage()
    return effect


def call_for_family_typed_or_team(element, team: str):
    """Search Basic of element OR Basic with team in name onto Bench."""
    from spirit.game.session.effects import is_basic_pokemon
    pred = has_team_in_name(team)
    el = getattr(element, "value", element)
    def match(c):
        if not is_basic_pokemon(c):
            return False
        if pred(c):
            return True
        types = c.get_attribute(AttrID.POKEMON_TYPES) or []
        # Hand cards may need def_for
        if not types:
            d = def_for(c.archetype_id)
            types = [t.value if hasattr(t, "value") else t
                     for t in (getattr(d, "elements", None) or [])]
        return el in types
    return search_to_bench(match, count=1, prompt="Choose a Basic Pokémon to Bench")


def thick_poison():
    """Heads: Confused+Poisoned; tails: Poisoned (2 counters on tails? text: Poisoned)."""
    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(1, "Thick Poison")
        await ctx.apply_special_condition(
            ctx.defender, SpecialConditions.POISONED)
        if results and results[0]:
            await ctx.apply_special_condition(
                ctx.defender, SpecialConditions.CONFUSED)
    return effect


def aqua_call(team: str = "Team Aqua", count: int = 3):
    """Search up to `count` team Pokémon into hand."""
    from spirit.game.session.effects import is_pokemon_card
    pred = has_team_in_name(team)
    def match(c):
        return is_pokemon_card(c) and pred(c)
    async def effect(ctx):
        picks = await ctx.search_deck(
            match, count=count, minimum=0,
            prompt=f"Choose up to {count} Pokémon with {team} in its name",
        )
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def thunderspark(amount: int = 10):
    """`amount` to each Benched (both sides) that has Energy attached."""
    async def effect(ctx):
        await ctx.deal_damage()
        for p in ctx.my_bench() + ctx.opponent_bench():
            if any(is_energy_card(c) for c in p.children):
                await ctx.deal_damage(amount, target=p, apply_modifiers=False)
    return effect


def chaos_crush():
    """If Confused, discard an Energy from Defending."""
    async def effect(ctx):
        await ctx.deal_damage()
        d = ctx.defender
        if d is None:
            return
        conds = d.get_attribute(AttrID.SPECIAL_CONDITIONS) or []
        if "Confused" in conds or SpecialConditions.CONFUSED.value in conds:
            await ctx.discard_energy_from(
                d, 1, prompt="Discard an Energy from the Defending Pokémon")
    return effect


def deep_impact():
    """If already damaged, Confuse."""
    async def effect(ctx):
        await ctx.deal_damage()
        d = ctx.defender
        if d is None:
            return
        if ctx.max_hp(d) - d.get_attribute(AttrID.HP, 0) > 0:
            await ctx.apply_special_condition(d, SpecialConditions.CONFUSED)
    return effect


def bonus_if_asleep(bonus: int, base: Optional[int] = None):
    from spirit.game.card_effects.attacks_common import (
        bonus_if, defender_has_condition,
    )
    return bonus_if(defender_has_condition(SpecialConditions.ASLEEP), bonus, base=base)


def flame_ball():
    """May move a Fire Energy from self to a Benched Pokémon."""
    async def effect(ctx):
        await ctx.deal_damage()
        fires = [c for c in ctx.attacker.children
                 if energy_provides_type(c, PokemonTypes.FIRE.value)]
        bench = ctx.my_bench()
        if fires and bench and await ctx.ask_yes_no(
                "Move a Fire Energy to 1 of your Benched Pokémon?"):
            picks = await ctx.choose_cards(fires, 1, minimum=1, prompt="Choose a Fire Energy")
            target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon")
            if picks and target is not None:
                await ctx.move_energy(picks[0], target)
    return effect


def hot_air(energy_type=PokemonTypes.FIRE):
    """Discard typed Energy; opponent switches Defending."""
    tv = getattr(energy_type, "value", energy_type)
    async def effect(ctx):
        await ctx.deal_damage()
        await ctx.discard_energy_from(
            ctx.attacker, 1,
            predicate=lambda c: energy_provides_type(c, tv),
            prompt="Discard a Fire Energy",
        )
        await opponent_switches(ctx)
    return effect


def magma_burn(mill: int = 1, energy_type=PokemonTypes.FIRE):
    """Mill opponent top; flip; on tails discard typed Energy from self."""
    tv = getattr(energy_type, "value", energy_type)
    async def effect(ctx):
        await ctx.deal_damage()
        top = ctx.deck_top(mill, player_id=ctx.opponent_id)
        await ctx.discard_cards(top)
        results = await ctx.flip_coins(1, "Magma Burn")
        if not (results and results[0]):
            await ctx.discard_energy_from(
                ctx.attacker, 1,
                predicate=lambda c: energy_provides_type(c, tv),
                prompt="Discard a Fire Energy",
            )
    return effect


def tm_miracle():
    """10 damage; choose 1 Special Condition to apply."""
    async def effect(ctx):
        await ctx.deal_damage(10)
        options = ["Asleep", "Burned", "Confused", "Paralyzed", "Poisoned"]
        conds = [
            SpecialConditions.ASLEEP, SpecialConditions.BURNED,
            SpecialConditions.CONFUSED, SpecialConditions.PARALYZED,
            SpecialConditions.POISONED,
        ]
        idx = await ctx.choose("Choose a Special Condition", options)
        if idx is None:
            idx = 0
        await ctx.apply_special_condition(ctx.defender, conds[idx])
    return effect


def tm_crushing_magma():
    """10 damage; put an Energy from Defending on bottom of opponent's deck."""
    async def effect(ctx):
        await ctx.deal_damage(10)
        d = ctx.defender
        if d is None:
            return
        energies = [c for c in d.children if is_energy_card(c)]
        if not energies:
            return
        picks = await ctx.choose_cards(
            energies, 1, minimum=1,
            prompt="Choose an Energy to put on the bottom of your opponent's deck")
        if picks:
            await ctx.put_on_bottom_of_deck(picks[0])
    return effect




def crush_per_energy(per: int = 30):
    """Flip a coin for each Energy attached; per * heads (Crush)."""
    from spirit.game.card_effects.attacks_common import flip_damage, count_energy
    async def effect(ctx):
        n = count_energy("self")(ctx)
        if n <= 0:
            await ctx.deal_damage(0)
            return
        # flip_damage with dynamic coins
        results = await ctx.flip_coins(n, "Crush")
        await ctx.deal_damage(per * sum(1 for r in results if r))
    return effect


def auxiliary_light():
    """Attach a basic Energy from hand to self; put 1 damage counter on self."""
    async def effect(ctx):
        pool = [c for c in ctx.hand() if is_basic_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=1, prompt="Attach a basic Energy from your hand")
        if not picks:
            return
        await ctx.attach_energy(picks[0], ctx.source)
        await ctx.deal_damage(20, target=ctx.source, apply_modifiers=False, as_counters=True)
    return effect


def power_shift(team: str = "Team Aqua"):
    """Move any number of basic Energy from one team Pokémon to another of yours."""
    pred = has_team_in_name(team)
    async def effect(ctx):
        donors = [p for p in ctx.my_pokemon_in_play()
                  if pred(p) and any(is_basic_energy_card(c) for c in p.children)]
        if not donors:
            return
        src = await ctx.choose_pokemon(donors, "Choose a Pokémon to move Energy from")
        if src is None:
            return
        pool = [c for c in src.children if is_basic_energy_card(c)]
        picks = await ctx.choose_cards(
            pool, len(pool), minimum=0,
            prompt="Choose basic Energy cards to move")
        if not picks:
            return
        dests = [p for p in ctx.my_pokemon_in_play() if p is not src]
        if not dests:
            return
        dest = await ctx.choose_pokemon(dests, "Choose a Pokémon to move Energy to")
        if dest is None:
            return
        for e in picks:
            await ctx.move_energy(e, dest)
    return effect


def overheat_attach():
    """Search discard for a basic Energy and attach to self; then 1 damage counter."""
    async def effect(ctx):
        pool = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
        if not pool:
            return
        picks = await ctx.choose_cards(
            pool, 1, minimum=1, prompt="Choose a basic Energy to attach")
        if not picks:
            return
        await ctx.attach_energy(picks[0], ctx.source)
        await ctx.deal_damage(20, target=ctx.source, apply_modifiers=False, as_counters=True)
    return effect


def magma_switch():
    """Move an Energy from one Team Magma Pokémon to another Team Magma Pokémon."""
    pred = has_team_in_name("Team Magma")
    async def effect(ctx):
        donors = [p for p in ctx.my_pokemon_in_play()
                  if pred(p) and any(is_energy_card(c) for c in p.children)]
        if not donors:
            return
        src = await ctx.choose_pokemon(donors, "Move Energy from which Team Magma Pokémon?")
        if src is None:
            return
        pool = [c for c in src.children if is_energy_card(c)]
        picks = await ctx.choose_cards(pool, 1, minimum=1, prompt="Choose an Energy to move")
        if not picks:
            return
        dests = [p for p in ctx.my_pokemon_in_play() if pred(p) and p is not src]
        if not dests:
            return
        dest = await ctx.choose_pokemon(dests, "Move Energy to which Team Magma Pokémon?")
        if dest is None:
            return
        await ctx.move_energy(picks[0], dest)
    return effect


def call_for_help(team: str = "Team Magma"):
    """If Active: search a team Pokémon into hand (Call for Help)."""
    from spirit.game.session.effects import is_pokemon_card
    pred = has_team_in_name(team)
    def match(c):
        return is_pokemon_card(c) and pred(c)
    async def effect(ctx):
        if not is_in_active_spot(ctx.source):
            return
        picks = await ctx.search_deck(
            match, count=1, minimum=0,
            prompt=f"Choose a Pokémon with {team} in its name",
        )
        await ctx.put_in_hand(picks, reveal=True)
        await ctx.shuffle_deck()
    return effect


def call_for_help_condition(team: str = "Team Magma"):
    from spirit.game.session.effects import is_pokemon_card
    pred = has_team_in_name(team)
    def cond(board, player_id, pokemon=None):
        if pokemon is None or not is_in_active_spot(pokemon):
            return False
        deck = board.find_player_area(player_id, "deck")
        return bool(deck) and any(is_pokemon_card(c) and pred(c) for c in deck.children)
    return cond


async def warp_point(ctx):
    """Opponent switches Active; then you switch Active."""
    await opponent_switches(ctx)
    await ctx.flush_choreography()
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose your new Active Pokémon")
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


async def genetic_memory(ctx):
    """Use any attack from this Pokémon's tucked Basic or Stage 1 Evolution
    card (Genetic Memory). Energy for the copied attack is not re-paid —
    Genetic Memory's own cost already covers the declaration."""
    from spirit.game.data_utils import Attack
    from spirit.game.models.board import PokemonEntity
    attacker = ctx.attacker
    if attacker is None:
        return
    candidates = []
    seen = set()
    for child in attacker.children:
        if not isinstance(child, PokemonEntity):
            continue
        stage = child.get_attribute(AttrID.STAGE)
        if stage not in (PokemonStage.BASIC.value, PokemonStage.STAGE1.value):
            continue
        definition = def_for(child.archetype_id)
        for ability in getattr(definition, "abilities", None) or []:
            if not isinstance(ability, Attack):
                continue
            key = (ability.title, ability.game_text)
            if key in seen:
                continue
            seen.add(key)
            candidates.append((child, ability))
    if not candidates:
        return
    picked = await ctx.choose_attack_to_copy(
        candidates,
        "Choose an attack from a Basic or Stage 1 Evolution card",
    )
    if picked is None:
        return
    _, chosen = picked
    await ctx.use_attack(chosen)

