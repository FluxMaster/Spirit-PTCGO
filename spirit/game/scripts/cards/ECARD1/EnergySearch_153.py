"""STUB: effect not implemented — do not guess mechanics.
Energy Search (ECARD1 #153): trainer effect stubbed.

Card text:
  - Search your deck for a basic Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="90e33c91-c781-5c1a-bf33-e47456d26dc5",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search"],
    subtypes=[],
    collector_number=153,
    set_code="ECARD1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
