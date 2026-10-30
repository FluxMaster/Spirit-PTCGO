"""STUB: effect not implemented — do not guess mechanics.
Switch (EX15 #83): trainer effect stubbed.

Card text:
  - Switch 1 of your Active Pokémon with 1 of your Benched Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d1d0834d-a5bb-5f5c-9df3-c31a90df8f11",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=83,
    set_code="EX15",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
