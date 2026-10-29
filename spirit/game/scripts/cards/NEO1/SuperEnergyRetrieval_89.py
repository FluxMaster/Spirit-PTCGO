"""STUB: effect not implemented — do not guess mechanics.
Super Energy Retrieval (NEO1 #89): trainer effect stubbed.

Card text:
  - Trade 2 of the other cards in your hand for 4 basic Energy cards from your discard pile. If you have fewer than 4 basic Energy cards there, take all of them.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="0d7c1281-b3da-5ce6-b7eb-1100930f7ad2",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperEnergyRetrieval.Name",
    display_name="Super Energy Retrieval",
    searchable_by=["Super Energy Retrieval"],
    subtypes=[],
    collector_number=89,
    set_code="NEO1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
