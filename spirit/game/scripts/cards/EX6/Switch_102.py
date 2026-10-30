"""STUB: effect not implemented — do not guess mechanics.
Switch (EX6 #102): trainer effect stubbed.

Card text:
  - Switch 1 of your Active Pokémon with 1 of your Benched Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="074a1710-3ef7-5c27-96d6-f07eb3200fae",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=102,
    set_code="EX6",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
