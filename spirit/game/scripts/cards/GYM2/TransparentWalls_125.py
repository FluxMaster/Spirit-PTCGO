"""STUB: effect not implemented — do not guess mechanics.
Transparent Walls (GYM2 #125): trainer effect stubbed.

Card text:
  - Until the end of your opponent's next turn, prevent all damage from attacks done to your Benched Pokémon. (Any other effects of attacks still happen.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d96ee441-d01d-5157-b81e-7f79037771a3",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TransparentWalls.Name",
    display_name="Transparent Walls",
    searchable_by=["Transparent Walls"],
    subtypes=[],
    collector_number=125,
    set_code="GYM2",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
