"""STUB: effect not implemented — do not guess mechanics.
Dual Ball (EX11 #89): trainer effect stubbed.

Card text:
  - Flip 2 coins. For each heads, search your deck for a Basic Pokémon card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ad50f0d1-553e-5a3b-a9b5-b01d8759ac8f",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DualBall.Name",
    display_name="Dual Ball",
    searchable_by=["Dual Ball", "Item"],
    subtypes=["Item"],
    collector_number=89,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
