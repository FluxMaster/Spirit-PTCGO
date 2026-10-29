"""Shared helpers for WOTC e-Card (Expedition / Aquapolis / Skyridge).

Card scripts stay thin data definitions; put non-trivial behavior here so
reprints across the three sets can import the same effect.
"""

from __future__ import annotations

from typing import Any, Callable, List, Optional

from spirit.game.attributes import AttrID, PokemonTypes, TrainerType
from spirit.game.content.definitions import Ability, Attack
from spirit.game.data_utils import def_for
from spirit.game.session.passives import Passive, carrier_pokemon


def no_special_conditions(board, player_id, pokemon=None) -> bool:
    """Poké-Power gate: unusable while the Pokemon has any Special Condition."""
    if pokemon is None:
        return False
    return not bool(pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS) or [])


def is_basic_non_baby(card) -> bool:
    """Dual Ball / similar: Basic Pokémon other than a Baby Pokémon."""
    from spirit.game.session.effects import is_basic_pokemon
    from spirit.game.data_utils import is_baby_pokemon
    return is_basic_pokemon(card) and not is_baby_pokemon(card.archetype_id)


class TechnicalMachinePassive(Passive):
    """Grants the TM's Attack(s) to the holder; discarded at end of owner turn.

    Pass the Attack (or list) that the TM printed. The Attack must already be
    registered on the TM card (ability_id assigned) — typically via putting it
    in TrainerCardDef.abilities so ABILITIES_BY_ID is populated.
    """

    def __init__(self, attacks: Any):
        if isinstance(attacks, (list, tuple)):
            self._attacks = list(attacks)
        else:
            self._attacks = [attacks]

    def granted_attacks(self, board, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return []
        # Only while this TM is still attached as the carrier.
        if carrier.get_attribute(AttrID.TRAINER_TYPE) != TrainerType.TECHNICAL_MACHINE.value:
            return []
        return list(self._attacks)




def pokemon_has_type(pokemon, pokemon_type: PokemonTypes) -> bool:
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return pokemon_type.value in types
