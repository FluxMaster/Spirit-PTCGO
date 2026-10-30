"""STUB: effect not implemented — do not guess mechanics.
Dusk Ball (DP2 #110): trainer effect stubbed.

Card text:
  - Look at the 7 cards from the bottom of your deck. Choose 1 Pokémon you find there, show it to your opponent, and put it into your hand. Put the remaining cards back on top of your deck. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="29d30129-414d-55d1-90f4-f77f7db81c8f",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DuskBall.Name",
    display_name="Dusk Ball",
    searchable_by=["Dusk Ball", "Item"],
    subtypes=["Item"],
    collector_number=110,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
