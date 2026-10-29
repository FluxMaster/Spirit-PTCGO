"""STUB: effect not implemented — do not guess mechanics.
Acro Bike (SM7 #178): trainer effect stubbed.

Card text:
  - Look at the top 2 cards of your deck and put 1 of them into your hand. Discard the other card.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="f82a585f-6923-591c-91e6-f3bcb85e341e",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AcroBike.Name",
    display_name="Acro Bike",
    searchable_by=["Acro Bike", "Item"],
    subtypes=["Item"],
    collector_number=178,
    set_code="SM7",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
