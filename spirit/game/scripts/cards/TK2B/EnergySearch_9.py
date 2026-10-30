"""STUB: effect not implemented — do not guess mechanics.
Energy Search (TK2B #9): trainer effect stubbed.

Card text:
  - Search your deck for a basic Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b552ef38-991e-5b9e-8136-a1cdf95901b9",
    key="TK2B",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=9,
    set_code="TK2B",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
