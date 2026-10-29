"""STUB: effect not implemented — do not guess mechanics.
Unit Energy {G}{R}{W} (SM5 #170): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card provides Colorless Energy.
  - While this card is attached to a Pokémon, it provides Grass, Fire, and Water Energy but provides only 1 Energy at a time.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="6045f77f-d7da-5ed4-864b-faea6c7c0f0b",
    key="SM5",
    name="Unit Energy {G}{R}{W}",
    display_name="Unit Energy {G}{R}{W}",
    searchable_by=["Unit Energy {G}{R}{W}", "Special"],
    subtypes=["Special"],
    collector_number=170,
    set_code="SM5",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
