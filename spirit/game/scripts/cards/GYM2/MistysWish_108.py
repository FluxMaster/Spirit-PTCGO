"""STUB: effect not implemented — do not guess mechanics.
Misty's Wish (GYM2 #108): trainer effect stubbed.

Card text:
  - Look at 1 of your Prize cards. Then, ask your opponent if you may switch that card with 1 of the cards in your hand. If your opponent accepts and if you have any other cards in your hand, switch those cards. If your opponent declines, return the Prize card face down and draw a card.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="8a3bf543-6627-5e5f-9529-cf757595acee",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysWish.Name",
    display_name="Misty's Wish",
    searchable_by=["Misty's Wish"],
    subtypes=[],
    collector_number=108,
    set_code="GYM2",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
