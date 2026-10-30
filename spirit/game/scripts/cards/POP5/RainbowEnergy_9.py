"""STUB: effect not implemented — do not guess mechanics.
δ Rainbow Energy (POP5 #9): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - δ Rainbow Energy provides Colorless Energy. While attached to a Pokémon that has δ on its card, δ Rainbow Energy provides every type of Energy but provides only 1 Energy at a time. (Has no effect other than providing Energy.)
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="be2a8ecd-9973-5d94-a989-7da8f9001ad5",
    key="POP5",
    name="δ Rainbow Energy",
    display_name="δ Rainbow Energy",
    searchable_by=["\u03b4 Rainbow Energy", "Special"],
    subtypes=["Special"],
    collector_number=9,
    set_code="POP5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
