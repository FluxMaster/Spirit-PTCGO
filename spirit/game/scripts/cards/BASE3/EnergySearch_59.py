"""STUB: effect not implemented — do not guess mechanics.
Energy Search (BASE3 #59): trainer effect stubbed.

Card text:
  - Search your deck for a basic Energy card and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="2931b336-c870-5403-b178-933d0e7905d4",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search"],
    subtypes=[],
    collector_number=59,
    set_code="BASE3",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
