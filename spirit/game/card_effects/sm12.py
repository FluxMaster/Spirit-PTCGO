"""Cosmic Eclipse (SM12) attack, ability, trainer, and stadium behaviors.

Card scripts stay thin data definitions; reprints import from here.
"""

import random

from spirit.game.attributes import (
    AttrID, PokemonTypes, SpecialConditions, TrainerType,
)
from spirit.game.data_utils import (
    TRAINER_EFFECTS_BY_GUID, def_for, is_tag_team, unimplemented,
)
from spirit.game.models.board import PokemonEntity
from spirit.game.session.constants import BENCH_CAPACITY
from spirit.game.session.effects import (
    full_stack,
    is_item_card,
    is_supporter_card,
    is_trainer_card,
)
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.card_effects.attacks_common import (
    _printed,
    bonus_if,
    condition_attack,
    count_discard,
    count_prizes_remaining,
    damage_per,
    discard_for_bonus,
    flip_damage,
    lock_defender_attacks,
    place_counters,
)
from spirit.game.card_effects.passives_common import takes_less_passive
from spirit.game.card_effects.sm3 import (
    is_fire_energy,
    is_gx_or_ex,
    is_water_energy,
)
from spirit.game.card_effects.sm5 import is_fairy_pokemon
from spirit.game.card_effects.sm6 import is_fighting_energy
from spirit.game.card_effects.sm10 import is_lightning_energy
from spirit.game.card_effects.support_common import (
    distribute_energy,
    look_top_attach_energy,
    recover_from_discard,
    search_to_bench,
    search_to_hand,
)
from spirit.game.card_effects.trainers import is_basic_energy_card, is_energy_card


_BURNED = SpecialConditions.BURNED
_PARALYZED = SpecialConditions.PARALYZED
_POISONED = SpecialConditions.POISONED
_CONFUSED = SpecialConditions.CONFUSED


def _logic_name(pokemon) -> str:
    return pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) or ""


def _display_name(card) -> str:
    return getattr(def_for(getattr(card, "archetype_id", None)), "display_name", "") or ""


def _playmat(entity):
    node = entity
    while node is not None and getattr(node, "parent", None) is not None:
        node = node.parent
    return node


def _hand(board, player_id):
    area = board.find_player_area(player_id, "hand")
    return list(area.children) if area else []


def _other_player(board, player_id):
    return next((p for p in board.player_ids if p != player_id), None)


def _is_unidentified_fossil(card) -> bool:
    return _display_name(card) == "Unidentified Fossil"


def _is_eevee(card) -> bool:
    return _logic_name(card) in ("Eevee", "EeveeGX") or _display_name(card) in (
        "Eevee", "Eevee-GX")


def _is_tag_team_card(card) -> bool:
    return is_tag_team(getattr(card, "archetype_id", None))


def _is_lillies_poke_doll(card) -> bool:
    return _display_name(card) == "Lillie's Poké Doll"


def _runnable_supporter(card) -> bool:
    if not is_supporter_card(card):
        return False
    effect = TRAINER_EFFECTS_BY_GUID.get((card.archetype_id or "").lower())
    return effect is not None and effect is not unimplemented


def _named_in_play_from(pokemon, *names) -> bool:
    playmat = _playmat(pokemon)
    owner = pokemon.owning_player_id
    wanted = set(names)
    for child in getattr(playmat, "children", []) or []:
        if getattr(child, "owning_player_id", None) != owner:
            continue
        for area in child.children:
            if area.get_attribute(AttrID.NAME) not in ("activePokemonArea", "bench"):
                continue
            for ally in area.children:
                if _logic_name(ally) in wanted:
                    return True
    return False


def _opponent_active_from(pokemon):
    playmat = _playmat(pokemon)
    owner = pokemon.owning_player_id
    for child in getattr(playmat, "children", []) or []:
        pid = getattr(child, "owning_player_id", None)
        if pid in (None, owner):
            continue
        for area in child.children:
            if area.get_attribute(AttrID.NAME) == "activePokemonArea":
                return next(iter(area.children), None)
    return None


def _own_stadium_in_play(ctx) -> bool:
    stadium = ctx.stadium_in_play()
    if stadium is None:
        return False
    owner = stadium.owning_player_id or getattr(stadium, "home_player_id", None)
    return owner == ctx.player_id


def _stadium_in_play(ctx) -> bool:
    return ctx.stadium_in_play() is not None


def _deck_at_most_3(ctx) -> bool:
    return len(ctx.deck()) <= 3


def _two_basic_energy_types(ctx) -> bool:
    types = set()
    attacker = ctx.attacker
    if attacker is None:
        return False
    for energy in ctx.attached_energies(attacker):
        if not is_basic_energy_card(energy):
            continue
        for energy_type in energy.get_attribute(AttrID.POKEMON_TYPES) or []:
            types.add(energy_type)
    return len(types) >= 2


def _has_water_energy(ctx) -> bool:
    attacker = ctx.attacker
    return attacker is not None and any(
        is_water_energy(energy) for energy in ctx.attached_energies(attacker))


def _played_tag_team_supporter(ctx) -> bool:
    return ctx.played_trainer_this_turn(
        lambda record: record[2] == TrainerType.SUPPORTER.value
        and is_tag_team(record[0])
    ) > 0


def _basic_fire_or_lightning(card) -> bool:
    return is_basic_energy_card(card) and (
        is_fire_energy(card) or is_lightning_energy(card))


# ----------------------------------------------------------------------
# Passives
# ----------------------------------------------------------------------

class DoubleTypePassive(Passive):
    """This Pokémon is Psychic and Fighting type."""

    def modify_pokemon_types(self, types, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return types
        return [PokemonTypes.PSYCHIC.value, PokemonTypes.FIGHTING.value]


class BeastBoostPassive(Passive):
    """This Pokémon's attacks do +20 to the opponent's Active per Prize taken."""

    def modify_damage_dealt(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.to_active):
            return
        attacker = calc.attacker
        if attacker is None or carrier_pokemon(carrier) is not attacker:
            return
        calc.amount += 20 * calc.board.prizes_taken(attacker.owning_player_id)


class BoilingBloodPassive(Passive):
    """Attacks cost ColorlessColorlessColorless less if the opponent has a GX/EX."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        opp = _other_player(board, pokemon.owning_player_id)
        if opp is None or not any(is_gx_or_ex(p) for p in board.pokemon_in_play(opp)):
            return cost
        if "Colorless" not in cost:
            return cost
        remaining = cost["Colorless"] - 3
        if remaining > 0:
            cost["Colorless"] = remaining
        else:
            del cost["Colorless"]
        return cost


class FightersRoarPassive(Passive):
    """Can evolve the turn it is played if the opponent's Active is GX/EX."""

    def may_evolve_early(self, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return False
        active = _opponent_active_from(pokemon)
        return active is not None and is_gx_or_ex(active)


def _sunne_protects(target, carrier) -> bool:
    if target.owning_player_id != carrier.owning_player_id:
        return False
    if _logic_name(target) not in ("Solgaleo", "Lunala"):
        return False
    return _named_in_play_from(carrier, "Lunala")


double_type_passive = DoubleTypePassive()
beast_boost_passive = BeastBoostPassive()
boiling_blood_passive = BoilingBloodPassive()
fighters_roar_passive = FightersRoarPassive()
armor_of_the_sunne_passive = takes_less_passive(
    50, protects=_sunne_protects, stack_key="armor_of_the_sunne")


# ----------------------------------------------------------------------
# Factory-backed attacks
# ----------------------------------------------------------------------

allergic_explosion_gx = condition_attack(_BURNED, _PARALYZED, _POISONED)
ancient_blast = damage_per(
    count_discard("mine", _is_unidentified_fossil), 50, base=20)
bye_bye_throw = discard_for_bonus(
    source="hand", max_count=2, per=60, base=0, optional=True,
    prompt="Discard up to 2 cards from your hand")
dazzling_blizzard = bonus_if(_own_stadium_in_play, 100)
dig_deep = recover_from_discard(
    is_energy_card, count=1, minimum=0,
    prompt="Choose an Energy card from your discard pile")
dragon_arcana = bonus_if(_two_basic_energy_types, 70)
dual_calling = search_to_hand(
    _is_tag_team_card, count=2, minimum=0,
    prompt="Choose up to 2 TAG TEAM cards")
eleventh_hour_tackle = bonus_if(_deck_at_most_3, 150)
fire_fling = recover_from_discard(
    is_fire_energy, count=4, minimum=0,
    prompt="Choose Fire Energy cards from your discard pile")
floral_invitation = search_to_hand(
    is_fairy_pokemon, count=2, minimum=0,
    prompt="Choose up to 2 Fairy Pokémon")
follow_my_tail = search_to_bench(
    _is_eevee, count=BENCH_CAPACITY,
    prompt="Choose Eevee or Eevee-GX to put onto your Bench.")
freezing_punch = bonus_if(_has_water_energy, 80)
iron_tail = flip_damage(until_tails=True, per_heads=100)
beloved_pulse = bonus_if(_played_tag_team_supporter, 80)
_look_top_8_energy = look_top_attach_energy(8, is_basic_energy_card)


# ----------------------------------------------------------------------
# Custom attacks / abilities
# ----------------------------------------------------------------------

async def _promote_if_needed(ctx, owner):
    if not await ctx.session._promote_new_active(owner):
        screen_name = ctx.session.players[owner].screen_name
        winner = ctx.opponent_id if owner == ctx.player_id else ctx.player_id
        await ctx.session.end_game(winner, f"{screen_name} has no Pokémon left")


async def backfire(ctx):
    await ctx.deal_damage()
    fires = [e for e in ctx.attached_energies(ctx.attacker) if is_fire_energy(e)]
    if not fires:
        return
    take = min(2, len(fires))
    picks = await ctx.choose_cards(
        fires, take, minimum=take,
        prompt="Put Fire Energy into your hand")
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


async def bag_slash(ctx):
    cards = await ctx.reveal_hand(
        of_player=ctx.opponent_id, to_player=ctx.player_id)
    items = [c for c in cards if is_item_card(c)]
    if not items:
        return
    picks = await ctx.choose_cards(
        items, 1, prompt="Discard an Item card from your opponent's hand")
    if picks:
        await ctx.discard_cards(picks)


async def balloon_burst(ctx):
    await ctx.deal_damage()
    attacker = ctx.attacker
    owner = attacker.owning_player_id or ctx.player_id
    was_active = attacker is ctx.board.active_pokemon(owner)
    await ctx.discard_cards(full_stack(attacker))
    if was_active:
        async def _promote():
            await _promote_if_needed(ctx, owner)
        ctx.deferred_actions.append(_promote)


async def brilliant_flare(ctx):
    await ctx.deal_damage()
    if not await ctx.ask_yes_no("Search your deck for up to 3 cards?"):
        return
    picks = await ctx.search_deck(
        None, count=3, minimum=0,
        prompt="Choose up to 3 cards to put into your hand.")
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


async def blow_away_bomb(ctx):
    """Roxie calls this after discarding a Koffing/Weezing from hand."""
    if not await ctx.ask_yes_no(
            "Put 1 damage counter on each of your opponent's Pokémon?"):
        return
    await place_counters(1, target="each_opponent")(ctx)


async def charming_stamp(ctx):
    pool = ctx.opponent_pokemon_in_play()
    if not pool:
        return
    target = await ctx.choose_pokemon(
        pool, "Choose 1 of your Pokémon", player_id=ctx.opponent_id)
    if target is not None:
        await ctx.deal_damage(90, target=target, apply_modifiers=False)


def cold_snap_condition(board, player_id, pokemon=None) -> bool:
    state = getattr(board, "turn_state", None)
    if state is None:
        return True
    return not any(title == "Cold Snap" for _, _, title in state.attacks_used_last_turn)


async def cold_snap(ctx):
    await ctx.deal_damage()
    ctx.lock_plays(ctx.opponent_id, is_trainer_card)


async def cross_break_gx(ctx):
    bench = ctx.opponent_bench()
    if not bench:
        return
    first = await ctx.choose_pokemon(
        bench, "Choose a Benched Pokémon to take 170 damage")
    if first is None:
        return
    await ctx.deal_damage(170, target=first, apply_modifiers=False)
    if ctx.played_trainer_this_turn("N's Resolve") <= 0:
        return
    rest = [p for p in ctx.opponent_bench() if p is not first]
    if not rest:
        return
    second = await ctx.choose_pokemon(
        rest, "Choose another Benched Pokémon to take 170 damage")
    if second is not None:
        await ctx.deal_damage(170, target=second, apply_modifiers=False)


async def desert_hurricane(ctx):
    extra = 120 if _stadium_in_play(ctx) else 0
    await ctx.deal_damage(_printed(ctx) + extra)
    if extra:
        await ctx.discard_stadium()


async def direct_dive(ctx):
    await ctx.discard_energy_from(
        ctx.attacker, 99, prompt="Discard all Energy from this Pokémon")
    bench = ctx.opponent_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(
        bench, "This attack does 100 damage to 1 of your opponent's Benched Pokémon")
    if target is not None:
        await ctx.deal_damage(100, target=target, apply_modifiers=False)


async def dirty_throw(ctx):
    if ctx.hand_size() == 0:
        return
    discarded = await ctx.discard_from_hand(
        1, minimum=1, prompt="Discard a card from your hand")
    if not discarded:
        return
    await ctx.deal_damage()


async def doll_swap(ctx):
    await ctx.deal_damage()
    pokemon = ctx.attacker
    owner = pokemon.owning_player_id or ctx.player_id
    was_active = pokemon is ctx.board.active_pokemon(owner)
    await ctx.put_in_hand(full_stack(pokemon), reveal=False)

    async def _replace():
        dolls = [c for c in ctx.hand(owner) if _is_lillies_poke_doll(c)]
        active_area = ctx.board.find_player_area(owner, "activePokemonArea")
        if dolls and isinstance(dolls[0], PokemonEntity) and active_area is not None:
            if await ctx.ask_yes_no(
                    "Play Lillie's Poké Doll as your new Active Pokémon?"):
                doll = dolls[0]
                if ctx.board.move_card(doll.entity_id, active_area.entity_id):
                    ctx.session.turn_state.mark_entered_play(doll.entity_id)
                    ctx.session.turn_state.became_active_turn[doll.entity_id] = (
                        ctx.session.turn_state.turn_number)
                    await ctx.session.fire_move_to_active_triggers(doll)
                    return
        if was_active:
            await _promote_if_needed(ctx, owner)

    ctx.deferred_actions.append(_replace)


async def drought(ctx):
    cards = [c for c in ctx.hand() if is_fighting_energy(c)]
    if not cards:
        return
    picks = await ctx.choose_cards(
        cards, 2, minimum=0, prompt="Choose up to 2 Fighting Energy cards")
    if not picks:
        return
    target = await ctx.choose_pokemon(
        ctx.my_pokemon_in_play(), "Choose a Pokémon to attach Energy to")
    if target is None:
        return
    for card in picks:
        await ctx.attach_energy(card, target)


async def explosive_fire_dance(ctx):
    if not await ctx.ask_yes_no("Look at the top 8 cards of your deck?"):
        return
    await _look_top_8_energy(ctx)


async def energy_assist(ctx):
    bench = ctx.my_bench()
    cards = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not bench or not cards:
        return
    picks = await ctx.choose_cards(
        cards, 2, minimum=0,
        prompt="Choose basic Energy cards to attach to your Benched Pokémon")
    if picks:
        await distribute_energy(ctx, picks, bench)


async def fabled_flarebolts(ctx):
    pool = []
    for pokemon in ctx.my_bench():
        for energy in ctx.attached_energies(pokemon):
            if _basic_fire_or_lightning(energy):
                pool.append(energy)
    picks = await ctx.choose_cards(
        pool, 3, minimum=0,
        prompt="Discard up to 3 basic Fire or Lightning Energy from your Benched Pokémon",
    ) if pool else []
    await ctx.discard_cards(picks)
    if picks:
        await ctx.deal_damage(90 * len(picks))


async def fireworks_bomb(ctx):
    n = 12 if count_prizes_remaining("opponent")(ctx) == 3 else 4
    await ctx.place_damage_counters(n)


async def fist_of_antiquity(ctx):
    if any(is_supporter_card(c) for c in ctx.discard_pile()):
        return
    await ctx.deal_damage()


async def flower_picking(ctx):
    hand = ctx.hand(ctx.opponent_id)
    if not hand:
        return
    if not await ctx.ask_yes_no(
            "Choose 2 random cards from your opponent's hand?"):
        return
    picks = random.sample(hand, min(2, len(hand)))
    await ctx.reveal_cards(picks, to_player=ctx.player_id)
    await ctx.shuffle_into_deck(picks, ctx.opponent_id)


async def grim_marking(ctx):
    if not ctx.ko_from_attack or not ctx.was_active_at_ko:
        return
    await ctx.place_damage_counters(4)


async def heavy_hold(ctx):
    await ctx.deal_damage()
    lock_defender_attacks(ctx)


def impersonation_condition(board, player_id, pokemon=None) -> bool:
    return any(_runnable_supporter(c) for c in _hand(board, player_id))


async def impersonation(ctx):
    candidates = [c for c in ctx.hand() if _runnable_supporter(c)]
    if not candidates:
        return
    picked = await ctx.choose_cards(
        candidates, 1, minimum=1,
        prompt="Discard a Supporter card and use its effect")
    if not picked:
        return
    await ctx.discard_cards(picked)
    effect = TRAINER_EFFECTS_BY_GUID[(picked[0].archetype_id or "").lower()]
    await effect(ctx)


async def improvisational_performance(ctx):
    n = ctx.hand_size()
    extra = 100 if n == 1 else 0
    await ctx.deal_damage(_printed(ctx) + extra)
    if n == 3:
        await ctx.apply_special_condition(ctx.defender, _CONFUSED)
    if n == 6:
        for pokemon in ctx.opponent_bench():
            await ctx.deal_damage(30, target=pokemon, apply_modifiers=False)


async def arf_arf_bark(ctx):
    discarded = ctx.source in ctx.discard_pile(ctx.player_id)
    if discarded and (not ctx.ko_from_attack or not ctx.was_active_at_ko):
        return
    active = ctx.opponent_active()
    if active is None or not ctx.attached_energies(active):
        return
    if not await ctx.ask_yes_no(
            "Discard an Energy from your opponent's Active Pokémon?"):
        return
    await ctx.discard_energy_from(
        active, 1, prompt="Choose an Energy to discard from the Defending Pokémon")
