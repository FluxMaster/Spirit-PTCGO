"""STUB: effect not implemented — do not guess mechanics.
Energy Search (TK2A #8): trainer effect stubbed.

Card text:
  - Search your deck for a basic Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="37bbe578-39e4-53d5-90b9-dfe34ed65898",
    key="TK2A",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=8,
    set_code="TK2A",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
