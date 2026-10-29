"""STUB: effect not implemented — do not guess mechanics.
Energy Loto (SM2 #122): trainer effect stubbed.

Card text:
  - Look at the top 7 cards of your deck. You may reveal an Energy card you find there and put it into your hand. Shuffle the other cards back into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="1a060d31-9c23-515d-8360-738b65244ff4",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyLoto.Name",
    display_name="Energy Loto",
    searchable_by=["Energy Loto", "Item"],
    subtypes=["Item"],
    collector_number=122,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
