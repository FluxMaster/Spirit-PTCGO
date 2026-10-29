"""STUB: effect not implemented — do not guess mechanics.
Energy Retrieval (BASE4 #110): trainer effect stubbed.

Card text:
  - Trade 1 of the other cards in your hand for up to 2 basic Energy cards from your discard pile.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="14f2bf5e-bc6c-5c61-b75d-69544763092f",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval"],
    subtypes=[],
    collector_number=110,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
