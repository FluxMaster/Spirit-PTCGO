"""STUB: effect not implemented — do not guess mechanics.
Switch (BASE4 #123): trainer effect stubbed.

Card text:
  - Switch 1 of your Benched Pokémon with your Active Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="171a5793-fc7f-5c22-8cc8-07ecb1ab02ba",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch"],
    subtypes=[],
    collector_number=123,
    set_code="BASE4",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
