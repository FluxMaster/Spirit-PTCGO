"""STUB: effect not implemented — do not guess mechanics.
Energy Flow (GYM1 #122): trainer effect stubbed.

Card text:
  - For each of your Pokémon, you may return any number of Energy cards attached to it to your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="9f399bfb-7cd0-5012-9ab0-577c3ad61020",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyFlow.Name",
    display_name="Energy Flow",
    searchable_by=["Energy Flow"],
    subtypes=[],
    collector_number=122,
    set_code="GYM1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
