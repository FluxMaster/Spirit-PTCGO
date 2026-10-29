"""STUB: effect not implemented — do not guess mechanics.
Recycle Energy (SM11 #257): special energy provides/passive/attach rules stubbed until matched to a known energy pattern.

Card text:
  - This card provides Colorless Energy.
  - If this card is discarded from play, put it into your hand instead of the discard pile.
"""

from spirit.game.data_utils import EnergyCardDef
from spirit.game.attributes import PokemonTypes, Rarities

card = EnergyCardDef(
    guid="90b445b5-deca-51e9-b280-ab6edd4fca0f",
    key="SM11",
    name="Recycle Energy",
    display_name="Recycle Energy",
    searchable_by=["Recycle Energy", "Special"],
    subtypes=["Special"],
    collector_number=257,
    set_code="SM11",
    rarity=Rarities.RareSecret,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    # STUB: special energy mechanics not implemented
)
