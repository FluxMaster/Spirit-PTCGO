"""STUB: effect not implemented — do not guess mechanics.
Computer Search (BASE4 #101): trainer effect stubbed.

Card text:
  - Discard 2 of the other cards from your hand in order to search your deck for any card and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="7c865218-6d19-5016-b199-e353d3542aff",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ComputerSearch.Name",
    display_name="Computer Search",
    searchable_by=["Computer Search"],
    subtypes=[],
    collector_number=101,
    set_code="BASE4",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
