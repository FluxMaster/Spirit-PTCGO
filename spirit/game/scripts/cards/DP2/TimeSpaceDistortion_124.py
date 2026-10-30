"""STUB: effect not implemented — do not guess mechanics.
Time-Space Distortion (DP2 #124): trainer effect stubbed.

Card text:
  - Flip 3 coins. For each heads, search your discard pile for a Pokémon, show it to your opponent, and put it into your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="9de91e32-e439-5bdf-b3b4-ff547d4ddbef",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TimeSpaceDistortion.Name",
    display_name="Time-Space Distortion",
    searchable_by=["Time-Space Distortion", "Item"],
    subtypes=["Item"],
    collector_number=124,
    set_code="DP2",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
