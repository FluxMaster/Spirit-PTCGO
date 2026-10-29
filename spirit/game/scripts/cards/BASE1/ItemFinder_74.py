"""STUB: effect not implemented — do not guess mechanics.
Item Finder (BASE1 #74): trainer effect stubbed.

Card text:
  - Discard 2 of the other cards from your hand in order to put a Trainer card from your discard pile into your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="614c8467-8be1-5f23-bb8b-989ddf3bf261",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ItemFinder.Name",
    display_name="Item Finder",
    searchable_by=["Item Finder"],
    subtypes=[],
    collector_number=74,
    set_code="BASE1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
