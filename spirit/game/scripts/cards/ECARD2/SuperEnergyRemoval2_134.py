"""STUB: effect not implemented — do not guess mechanics.
Super Energy Removal 2 (ECARD2 #134): trainer effect stubbed.

Card text:
  - Flip 2 coins. If both are heads, discard all Energy cards attached to the Defending Pokémon. If both are tails, discard all Energy cards attached to your Active Pokémon. If 1 is heads and 1 is tails, this card does nothing.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="50ff5f7d-665a-5af0-b15e-5321358a14f4",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperEnergyRemoval2.Name",
    display_name="Super Energy Removal 2",
    searchable_by=["Super Energy Removal 2"],
    subtypes=[],
    collector_number=134,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
