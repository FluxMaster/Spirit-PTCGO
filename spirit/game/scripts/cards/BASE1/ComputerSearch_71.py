"""STUB: effect not implemented — do not guess mechanics.
Computer Search (BASE1 #71): trainer effect stubbed.

Card text:
  - Discard 2 of the other cards from your hand in order to search your deck for any card and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="cbeac06c-8bf8-5c29-a596-955ff0f2445c",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ComputerSearch.Name",
    display_name="Computer Search",
    searchable_by=["Computer Search"],
    subtypes=[],
    collector_number=71,
    set_code="BASE1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
