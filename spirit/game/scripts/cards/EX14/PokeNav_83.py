"""STUB: effect not implemented — do not guess mechanics.
PokéNav (EX14 #83): trainer effect stubbed.

Card text:
  - Look at the top 3 cards of your deck, and choose a Basic Pokémon, Evolution card, or Energy card. Show it to your opponent and put it into your hand. Put the 2 other cards back on top of your deck in any order.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ca85ee98-a445-53c9-9a7e-57cc8972f51c",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeNav.Name",
    display_name="PokéNav",
    searchable_by=["Pok\u00e9Nav", "Item"],
    subtypes=["Item"],
    collector_number=83,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
