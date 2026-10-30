"""STUB: effect not implemented — do not guess mechanics.
Energy Switch (EX16 #75): trainer effect stubbed.

Card text:
  - Move a basic Energy card attached to 1 of your Pokémon to another of your Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="5514293e-8dd8-5cc3-9ffe-17b6c5e26665",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=75,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
