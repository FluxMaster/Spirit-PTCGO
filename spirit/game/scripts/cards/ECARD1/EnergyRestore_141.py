"""STUB: effect not implemented — do not guess mechanics.
Energy Restore (ECARD1 #141): trainer effect stubbed.

Card text:
  - Flip 3 coins. For each heads, put a Basic Energy card from your discard pile into your hand. If you don't have that many basic Energy cards in your discard pile, put all of them into your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ff947b34-c2be-5a79-918c-f3faa70d4735",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRestore.Name",
    display_name="Energy Restore",
    searchable_by=["Energy Restore"],
    subtypes=[],
    collector_number=141,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
