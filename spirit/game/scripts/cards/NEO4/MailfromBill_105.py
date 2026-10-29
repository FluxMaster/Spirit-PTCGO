"""STUB: effect not implemented — do not guess mechanics.
Mail from Bill (NEO4 #105): trainer effect stubbed.

Card text:
  - You can't play this card if you have 5 or more cards in your hand (including this one). Draw cards until you have exactly 4 cards in your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="27303010-e742-528f-b79a-fd21900a16c2",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MailfromBill.Name",
    display_name="Mail from Bill",
    searchable_by=["Mail from Bill"],
    subtypes=[],
    collector_number=105,
    set_code="NEO4",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
