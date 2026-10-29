"""STUB: effect not implemented — do not guess mechanics.
Peeking Red Card (SM4 #97): trainer effect stubbed.

Card text:
  - Your opponent reveals their hand. You may have your opponent count the cards in their hand, shuffle those cards into their deck, then draw that many cards.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b818ec09-ef33-5424-bd54-16aa869707a6",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PeekingRedCard.Name",
    display_name="Peeking Red Card",
    searchable_by=["Peeking Red Card", "Item"],
    subtypes=["Item"],
    collector_number=97,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
