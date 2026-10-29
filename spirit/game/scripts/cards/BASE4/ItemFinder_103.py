"""STUB: effect not implemented — do not guess mechanics.
Item Finder (BASE4 #103): trainer effect stubbed.

Card text:
  - Discard 2 of the other cards from your hand in order to put a Trainer card from your discard pile into your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="cdb60c14-3d35-5e77-b80e-0a88e9703f14",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ItemFinder.Name",
    display_name="Item Finder",
    searchable_by=["Item Finder"],
    subtypes=[],
    collector_number=103,
    set_code="BASE4",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
