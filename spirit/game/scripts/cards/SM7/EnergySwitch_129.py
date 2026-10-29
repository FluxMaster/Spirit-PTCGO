"""STUB: effect not implemented — do not guess mechanics.
Energy Switch (SM7 #129): trainer effect stubbed.

Card text:
  - Move a basic Energy from 1 of your Pokémon to another of your Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d0b23b56-24c4-5fe3-b9ca-5112a8618520",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySwitch.Name",
    display_name="Energy Switch",
    searchable_by=["Energy Switch", "Item"],
    subtypes=["Item"],
    collector_number=129,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
