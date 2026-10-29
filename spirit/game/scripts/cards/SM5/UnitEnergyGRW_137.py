"""STUB: effect not implemented — do not guess mechanics.
Unit Energy {G}{R}{W} (SM5 #137): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card provides Colorless Energy.
  - While this card is attached to a Pokémon, it provides Grass, Fire, and Water Energy but provides only 1 Energy at a time.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="78ef6670-b1f2-537d-9da9-f631e193cb2f",
    key="SM5",
    name="Unit Energy {G}{R}{W}",
    display_name="Unit Energy {G}{R}{W}",
    searchable_by=["Unit Energy {G}{R}{W}", "Special"],
    subtypes=["Special"],
    collector_number=137,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
