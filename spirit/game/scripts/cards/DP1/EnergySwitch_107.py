"""STUB: effect not implemented — do not guess mechanics.
Energy Switch (DP1 #107): trainer effect stubbed.

Card text:
  - Move a basic Energy card attached to 1 of your Pokémon to another of your Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e298d179-ea27-5e2d-9abc-6522c0a21cb1",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=107,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
