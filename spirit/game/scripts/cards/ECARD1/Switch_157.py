"""STUB: effect not implemented — do not guess mechanics.
Switch (ECARD1 #157): trainer effect stubbed.

Card text:
  - Switch your Active Pokémon with 1 of your Benched Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="fff7fde6-46d5-5b23-b648-2904abcdc49d",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch"],
    subtypes=[],
    collector_number=157,
    set_code="ECARD1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
