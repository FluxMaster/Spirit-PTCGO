"""STUB: effect not implemented — do not guess mechanics.
Switch (BASE1 #95): trainer effect stubbed.

Card text:
  - Switch 1 of your own Benched Pokémon with your Active Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="bc14dcbb-a491-5309-8c29-31cddb6a371b",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch"],
    subtypes=[],
    collector_number=95,
    set_code="BASE1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
