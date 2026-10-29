"""STUB: effect not implemented — do not guess mechanics.
Radio Tower (NEO4 #95): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Once during each player's turn (before attacking), that player may look at the top 2 cards of his or her deck and put them back in the same order.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="895f22af-3f5c-50da-96c1-2dcf5ad8327e",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RadioTower.Name",
    display_name="Radio Tower",
    searchable_by=["Radio Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=95,
    set_code="NEO4",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
