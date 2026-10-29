"""STUB: effect not implemented — do not guess mechanics.
Reset Stamp (SM11 #206): trainer effect stubbed.

Card text:
  - Your opponent shuffles their hand into their deck and draws a card for each of their remaining Prize cards.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="3e8493ff-cb8a-56ea-9246-910bd2e970ad",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ResetStamp.Name",
    display_name="Reset Stamp",
    searchable_by=["Reset Stamp", "Item"],
    subtypes=["Item"],
    collector_number=206,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
