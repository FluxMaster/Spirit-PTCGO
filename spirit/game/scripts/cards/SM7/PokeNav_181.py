"""STUB: effect not implemented — do not guess mechanics.
PokéNav (SM7 #181): trainer effect stubbed.

Card text:
  - Look at the top 3 cards of your deck. You may reveal a Pokémon or Energy card you find there and put it into your hand. Put the other cards back in any order.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="457c7e1e-431b-5ea9-a9a2-aafba43a9d11",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeNav.Name",
    display_name="PokéNav",
    searchable_by=["Pok\u00e9Nav", "Item"],
    subtypes=["Item"],
    collector_number=181,
    set_code="SM7",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
