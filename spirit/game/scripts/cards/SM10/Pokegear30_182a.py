"""STUB: effect not implemented — do not guess mechanics.
Pokégear 3.0 (SM10 #182a): trainer effect stubbed.

Card text:
  - Look at the top 7 cards of your deck. You may reveal a Supporter card you find there and put it into your hand. Shuffle the other cards back into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="be292e28-ece9-597f-bd4b-3e884acb23a1",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokegear30.Name",
    display_name="Pokégear 3.0",
    searchable_by=["Pok\u00e9gear 3.0", "Item"],
    subtypes=["Item"],
    collector_number=235,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
