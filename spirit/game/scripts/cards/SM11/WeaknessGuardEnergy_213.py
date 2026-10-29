"""STUB: effect not implemented — do not guess mechanics.
Weakness Guard Energy (SM11 #213): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card provides Colorless Energy.
  - The Pokémon this card is attached to has no Weakness.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="82c44a85-69c0-5db6-8c25-2eb386245373",
    key="SM11",
    name="Weakness Guard Energy",
    display_name="Weakness Guard Energy",
    searchable_by=["Weakness Guard Energy", "Special"],
    subtypes=["Special"],
    collector_number=213,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
