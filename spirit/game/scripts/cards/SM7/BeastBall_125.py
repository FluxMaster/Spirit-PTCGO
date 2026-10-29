"""STUB: effect not implemented — do not guess mechanics.
Beast Ball (SM7 #125): trainer effect stubbed.

Card text:
  - Look at your face-down Prize cards. You may reveal an Ultra Beast card you find there, put it into your hand, and put this Beast Ball in its place. (If you don't reveal an Ultra Beast card, put this card in the discard pile.) Then, shuffle your face-down Prize cards.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="97afc8bc-4058-5226-a109-58e7ee8cfa6a",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeastBall.Name",
    display_name="Beast Ball",
    searchable_by=["Beast Ball", "Item"],
    subtypes=["Item"],
    collector_number=125,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
