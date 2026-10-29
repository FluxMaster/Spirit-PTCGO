"""STUB: effect not implemented — do not guess mechanics.
Pokégear 3.0 (SM10 #182): trainer effect stubbed.

Card text:
  - Look at the top 7 cards of your deck. You may reveal a Supporter card you find there and put it into your hand. Shuffle the other cards back into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="53217e55-56ea-5504-b940-aefcee4d5f36",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Pokegear30.Name",
    display_name="Pokégear 3.0",
    searchable_by=["Pok\u00e9gear 3.0", "Item"],
    subtypes=["Item"],
    collector_number=182,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
