"""STUB: effect not implemented — do not guess mechanics.
Peeking Red Card (SM5 #169): trainer effect stubbed.

Card text:
  - Your opponent reveals their hand. You may have your opponent count the cards in their hand, shuffle those cards into their deck, then draw that many cards.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="a6084b29-e8d0-5287-93c4-1d2c316dfec4",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PeekingRedCard.Name",
    display_name="Peeking Red Card",
    searchable_by=["Peeking Red Card", "Item"],
    subtypes=["Item"],
    collector_number=169,
    set_code="SM5",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
