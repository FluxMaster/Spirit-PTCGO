"""STUB: effect not implemented — do not guess mechanics.
Energy Search (TK1A #9): trainer effect stubbed.

Card text:
  - Search your deck for a basic Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e8bb5119-9817-54f4-a0e0-097fef27af5b",
    key="TK1A",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=9,
    set_code="TK1A",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
