"""STUB: effect not implemented — do not guess mechanics.
Crystal Energy (ECARD2 #146): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - Crystal Energy provides 1 Energy of all types (colors) of basic Energy cards attached to the Pokémon Crystal Energy is attached to. If there are no basic Energy cards attached to the Pokémon Crystal Energy is attached to, Crystal Energy provides Colorless Energy.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="4aa45df5-96c8-5d0d-909a-ccabce153575",
    key="ECARD2",
    name="Crystal Energy",
    display_name="Crystal Energy",
    searchable_by=["Crystal Energy", "Special"],
    subtypes=["Special"],
    collector_number=146,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
