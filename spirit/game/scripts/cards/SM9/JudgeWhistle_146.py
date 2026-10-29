"""STUB: effect not implemented — do not guess mechanics.
Judge Whistle (SM9 #146): trainer effect stubbed.

Card text:
  - Choose 1:
• Draw a card
• Put a Judge card from your discard pile into your hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ad58126a-a0ae-58e9-a4ec-db600586365d",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JudgeWhistle.Name",
    display_name="Judge Whistle",
    searchable_by=["Judge Whistle", "Item"],
    subtypes=["Item"],
    collector_number=146,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
