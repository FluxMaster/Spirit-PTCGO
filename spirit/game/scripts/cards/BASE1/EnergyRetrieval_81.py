"""STUB: effect not implemented — do not guess mechanics.
Energy Retrieval (BASE1 #81): trainer effect stubbed.

Card text:
  - Trade 1 of the other cards in your hand for up to 2 basic Energy cards from your discard pile.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="0b0dab82-1de7-59c4-8e6e-4b2aa650f8ac",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRetrieval.Name",
    display_name="Energy Retrieval",
    searchable_by=["Energy Retrieval"],
    subtypes=[],
    collector_number=81,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
