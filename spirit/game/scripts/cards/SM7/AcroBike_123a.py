"""STUB: effect not implemented — do not guess mechanics.
Acro Bike (SM7 #123a): trainer effect stubbed.

Card text:
  - Look at the top 2 cards of your deck and put 1 of them into your hand. Discard the other card.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d6a497b6-2857-5a3f-b530-a25a7cff95f4",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AcroBike.Name",
    display_name="Acro Bike",
    searchable_by=["Acro Bike", "Item"],
    subtypes=["Item"],
    collector_number=185,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
