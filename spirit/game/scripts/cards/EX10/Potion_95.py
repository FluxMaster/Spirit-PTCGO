"""STUB: effect not implemented — do not guess mechanics.
Potion (EX10 #95): trainer effect stubbed.

Card text:
  - Remove 2 damage counters from 1 of your Pokémon (remove 1 damage counter if that Pokémon has only 1).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d40b8509-300e-57bd-89d3-a5a9f26d23bb",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=95,
    set_code="EX10",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
