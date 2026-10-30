"""STUB: effect not implemented — do not guess mechanics.
Dual Ball (EX4 #72): trainer effect stubbed.

Card text:
  - Flip 2 coins. For each heads, search your deck for a Basic Pokémon card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="3daf1ffd-2d47-5a87-9334-14e8fbe79097",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DualBall.Name",
    display_name="Dual Ball",
    searchable_by=["Dual Ball", "Item"],
    subtypes=["Item"],
    collector_number=72,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
