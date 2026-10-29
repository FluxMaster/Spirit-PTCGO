"""Shared helpers for the EX era (Ruby & Sapphire through Power Keepers).

Card scripts stay thin data definitions; put non-trivial EX-era behavior here
so reprints across EX / Nintendo promos / POP can import the same effect.

Era themes: Pokémon-ex (2 prizes via subtype ``ex``), Poké-Powers / Poké-Bodies,
dual types, δ Delta Species, Holon Energies, Pokémon Star, Dark / owner's /
Rocket's Pokémon.
"""

from __future__ import annotations

from typing import Any, Callable, Optional

from spirit.game.attributes import AbilityTypes, AttrID, PokemonTypes, SpecialConditions
from spirit.game.card_effects.attacks_common import (
    count_energy, discard_random_from_hand, lock_all_attacks,
)
from spirit.game.card_effects.passives_common import (
    apply_own_next_turn_boost, is_in_active_spot,
)
from spirit.game.card_effects.pokemon import energy_provides_type, is_energy_card
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.data_utils import def_for, subtypes_for
from spirit.game.session.effects import (
    full_stack, is_basic_pokemon, is_evolution_pokemon,
)
from spirit.game.session.passives import Passive, carrier_pokemon

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


def defender_is_ex(ctx) -> bool:
    """cond_fn: the Defending Pokémon is a Pokémon-ex (subtype ``ex``)."""
    defender = ctx.defender
    return defender is not None and "ex" in subtypes_for(defender.archetype_id)


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


def flip_tails_discard_energy(energy_type=None):
    """Printed damage; flip a coin. If tails, discard 1 Energy of
    `energy_type` (or any Energy) from this Pokémon (Fireworks)."""
    type_value = getattr(energy_type, "value", energy_type)
    pred = (lambda c: energy_provides_type(c, type_value)) \
        if type_value is not None else None

    async def effect(ctx):
        await ctx.deal_damage()
        results = await ctx.flip_coins(
            1, ctx.ability.title if ctx.ability else "")
        if results and not results[0]:
            await ctx.discard_energy_from(
                ctx.attacker, 1, predicate=pred,
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
