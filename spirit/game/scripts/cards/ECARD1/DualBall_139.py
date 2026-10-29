"""STUB: effect not implemented — do not guess mechanics.
Dual Ball (ECARD1 #139): trainer effect stubbed.

Card text:
  - Flip 2 coins. For each heads, search your deck for a Basic Pokémon card other than a Baby Pokémon card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e6f4e260-36e7-5ad7-95a4-a64421839dd8",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DualBall.Name",
    display_name="Dual Ball",
    searchable_by=["Dual Ball"],
    subtypes=[],
    collector_number=139,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
