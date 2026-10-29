"""STUB: effect not implemented — do not guess mechanics.
Warp Point (GYM2 #126): trainer effect stubbed.

Card text:
  - If your opponent has any Benched Pokémon, he or she chooses 1 of them and switches it with his or her Active Pokémon, then, if you have any Benched Pokémon, you switch 1 of them with your Active Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="7a2778a7-31ec-5e8c-b37b-418e1b4e2274",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WarpPoint.Name",
    display_name="Warp Point",
    searchable_by=["Warp Point"],
    subtypes=[],
    collector_number=126,
    set_code="GYM2",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
