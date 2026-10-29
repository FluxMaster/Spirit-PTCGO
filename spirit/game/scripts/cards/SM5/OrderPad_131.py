"""STUB: effect not implemented — do not guess mechanics.
Order Pad (SM5 #131): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, search your deck for an Item card, reveal it, and put it into your hand. Then, shuffle your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ea39c280-408d-597b-9a7d-d7586e5ea8e2",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OrderPad.Name",
    display_name="Order Pad",
    searchable_by=["Order Pad", "Item"],
    subtypes=["Item"],
    collector_number=131,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
