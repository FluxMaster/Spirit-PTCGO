"""STUB: effect not implemented — do not guess mechanics.
Energy Removal (BASE1 #92): trainer effect stubbed.

Card text:
  - Choose 1 Energy card attached to 1 of your opponent's Pokémon and discard it.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ba29102d-bffa-50fc-9029-2423e5d1772b",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRemoval.Name",
    display_name="Energy Removal",
    searchable_by=["Energy Removal"],
    subtypes=[],
    collector_number=92,
    set_code="BASE1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
