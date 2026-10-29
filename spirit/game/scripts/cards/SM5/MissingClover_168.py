"""STUB: effect not implemented — do not guess mechanics.
Missing Clover (SM5 #168): trainer effect stubbed.

Card text:
  - You may play 4 Missing Clover cards at once.
• If you played 1 card, look at the top card of your deck.
• If you played 4 cards, take a Prize card. (This effect works one time for 4 cards.)
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="3fdc9e9b-1d3c-54a7-8dbf-0bc6e47e86ad",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MissingClover.Name",
    display_name="Missing Clover",
    searchable_by=["Missing Clover", "Item"],
    subtypes=["Item"],
    collector_number=168,
    set_code="SM5",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
