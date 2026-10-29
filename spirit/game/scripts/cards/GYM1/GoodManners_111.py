"""STUB: effect not implemented — do not guess mechanics.
Good Manners (GYM1 #111): trainer effect stubbed.

Card text:
  - In order to play this card, you can't have any Basic Pokémon cards in your hand. Show your hand to your opponent, then search your deck for a Basic Pokémon card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ebb39525-5bf3-5a07-a618-0b40b165e1ad",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GoodManners.Name",
    display_name="Good Manners",
    searchable_by=["Good Manners"],
    subtypes=[],
    collector_number=111,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
