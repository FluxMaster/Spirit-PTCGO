"""STUB: effect not implemented — do not guess mechanics.
Lure Ball (ECARD3 #128): trainer effect stubbed.

Card text:
  - Flip 3 coins. For each heads, choose an Evolution card from your discard pile, show it to your opponent, and put it into your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="485fd11c-7e32-5770-a251-d19e8c24ae30",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LureBall.Name",
    display_name="Lure Ball",
    searchable_by=["Lure Ball"],
    subtypes=[],
    collector_number=128,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
