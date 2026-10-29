"""STUB: effect not implemented — do not guess mechanics.
Erika (GYM1 #100): trainer effect stubbed.

Card text:
  - You may draw up to 3 cards, then your opponent may draw up to 3 cards.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="fe02825e-4cbe-5bc4-a87c-c7b44dc67364",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Erika.Name",
    display_name="Erika",
    searchable_by=["Erika"],
    subtypes=[],
    collector_number=100,
    set_code="GYM1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
