"""STUB: effect not implemented — do not guess mechanics.
Judge Whistle (SM9 #194): trainer effect stubbed.

Card text:
  - Choose 1:
• Draw a card
• Put a Judge card from your discard pile into your hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="86f89d7a-66b7-5155-bf49-5f7aa8fe4274",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JudgeWhistle.Name",
    display_name="Judge Whistle",
    searchable_by=["Judge Whistle", "Item"],
    subtypes=["Item"],
    collector_number=194,
    set_code="SM9",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
