"""STUB: effect not implemented — do not guess mechanics.
Warp Point (ECARD1 #152): trainer effect stubbed.

Card text:
  - Your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon, if any; then you switch your Active Pokémon with 1 of your Benched Pokémon, if any.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ef7ff778-e9c7-5a1c-bc15-f4dae5db4b02",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WarpPoint.Name",
    display_name="Warp Point",
    searchable_by=["Warp Point"],
    subtypes=[],
    collector_number=152,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
