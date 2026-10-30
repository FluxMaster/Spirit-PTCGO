"""STUB: effect not implemented — do not guess mechanics.
Super Scoop Up (EX6 #99): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, return 1 of your Pokémon and all cards attached to it to your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="841eb7e9-b705-5ba1-a513-5f592b470660",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=99,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
