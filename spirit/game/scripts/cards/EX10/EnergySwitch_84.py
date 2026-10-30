"""STUB: effect not implemented — do not guess mechanics.
Energy Switch (EX10 #84): trainer effect stubbed.

Card text:
  - Move a basic Energy card attached to 1 of your Pokémon to another of your Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="54356142-9853-54bf-a5d7-1bbc00cdd357",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=84,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
