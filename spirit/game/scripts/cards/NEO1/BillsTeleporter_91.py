"""STUB: effect not implemented — do not guess mechanics.
Bill's Teleporter (NEO1 #91): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, draw 4 cards.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="47e96095-de5b-5f8d-8798-45ccfed56b02",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsTeleporter.Name",
    display_name="Bill's Teleporter",
    searchable_by=["Bill's Teleporter"],
    subtypes=[],
    collector_number=91,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
