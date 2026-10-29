"""STUB: effect not implemented — do not guess mechanics.
PokéNav (SM7 #140): trainer effect stubbed.

Card text:
  - Look at the top 3 cards of your deck. You may reveal a Pokémon or Energy card you find there and put it into your hand. Put the other cards back in any order.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="04c8d539-e29e-5004-9b73-2a8b785cbc48",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeNav.Name",
    display_name="PokéNav",
    searchable_by=["Pok\u00e9Nav", "Item"],
    subtypes=["Item"],
    collector_number=140,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
