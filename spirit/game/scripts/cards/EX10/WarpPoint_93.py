"""STUB: effect not implemented — do not guess mechanics.
Warp Point (EX10 #93): trainer effect stubbed.

Card text:
  - Your opponent switches 1 of his or her Defending Pokémon with 1 of his or her Benched Pokémon, if any. You switch 1 of your Active Pokémon with 1 of your Benched Pokémon, if any.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="8fd3b23a-a76e-53b6-b28a-de2314b6bd33",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WarpPoint.Name",
    display_name="Warp Point",
    searchable_by=["Warp Point", "Item"],
    subtypes=["Item"],
    collector_number=93,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
