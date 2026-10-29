"""STUB: effect not implemented — do not guess mechanics.
Reset Stamp (SM11 #253): trainer effect stubbed.

Card text:
  - Your opponent shuffles their hand into their deck and draws a card for each of their remaining Prize cards.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="6c3be686-33f1-51fd-8b2f-126b0e7481a0",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ResetStamp.Name",
    display_name="Reset Stamp",
    searchable_by=["Reset Stamp", "Item"],
    subtypes=["Item"],
    collector_number=253,
    set_code="SM11",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
