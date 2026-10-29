"""STUB: effect not implemented — do not guess mechanics.
Energy Removal 2 (ECARD1 #140): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, choose 1 Energy card attached to 1 of your opponent's Pokémon and discard it.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d1e0df22-cbc3-593d-a852-55e0b47f0abf",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRemoval2.Name",
    display_name="Energy Removal 2",
    searchable_by=["Energy Removal 2"],
    subtypes=[],
    collector_number=140,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
