"""STUB: effect not implemented — do not guess mechanics.
Missing Clover (SM5 #129): trainer effect stubbed.

Card text:
  - You may play 4 Missing Clover cards at once.
• If you played 1 card, look at the top card of your deck.
• If you played 4 cards, take a Prize card. (This effect works one time for 4 cards.)
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="f4f75452-c5dd-52c5-bc11-0c8d9522f3bd",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MissingClover.Name",
    display_name="Missing Clover",
    searchable_by=["Missing Clover", "Item"],
    subtypes=["Item"],
    collector_number=129,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
