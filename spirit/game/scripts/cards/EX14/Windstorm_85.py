"""STUB: effect not implemented — do not guess mechanics.
Windstorm (EX14 #85): trainer effect stubbed.

Card text:
  - Choose up to 2 in any combination of Pokémon Tool cards and Stadium cards in play (both yours and your opponent's) and discard them.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="db3d3b1c-9b4b-5089-989b-7f0711b2423d",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Windstorm.Name",
    display_name="Windstorm",
    searchable_by=["Windstorm", "Item"],
    subtypes=["Item"],
    collector_number=85,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
