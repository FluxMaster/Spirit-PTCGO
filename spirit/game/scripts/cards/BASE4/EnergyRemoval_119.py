"""STUB: effect not implemented — do not guess mechanics.
Energy Removal (BASE4 #119): trainer effect stubbed.

Card text:
  - Choose 1 Energy card attached to 1 of your opponent's Pokémon and discard it.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="445c272e-28dd-5f7a-aaeb-ac6bd41aa74d",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRemoval.Name",
    display_name="Energy Removal",
    searchable_by=["Energy Removal"],
    subtypes=[],
    collector_number=119,
    set_code="BASE4",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
