"""STUB: effect not implemented — do not guess mechanics.
R Energy (EX7 #95): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - R Energy can be attached only to a Pokémon that has Dark or Rocket's in its name. While in play, R Energy provides 2 Darkness Energy. (Doesn't count as a basic Energy card.) If the Pokémon R Energy is attached to attacks, the attack does 10 more damage to the Active Pokémon (before applying Weakness and Resistance). When your turn ends, discard R Energy.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="118013fc-9de9-5215-bd40-6bfd7e48e008",
    key="EX7",
    name="R Energy",
    display_name="R Energy",
    searchable_by=["R Energy", "Special"],
    subtypes=["Special"],
    collector_number=95,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
