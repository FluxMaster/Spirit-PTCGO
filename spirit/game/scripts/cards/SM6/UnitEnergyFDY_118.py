"""STUB: effect not implemented — do not guess mechanics.
Unit Energy {F}{D}{Y} (SM6 #118): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card provides Colorless Energy.
  - While this card is attached to a Pokémon, it provides Fighting, Darkness, and Fairy Energy but provides only 1 Energy at a time.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="495d53df-e84d-5eaf-9104-d6389dddac5f",
    key="SM6",
    name="Unit Energy {F}{D}{Y}",
    display_name="Unit Energy {F}{D}{Y}",
    searchable_by=["Unit Energy {F}{D}{Y}", "Special"],
    subtypes=["Special"],
    collector_number=118,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
