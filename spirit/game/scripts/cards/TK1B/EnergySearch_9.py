"""STUB: effect not implemented — do not guess mechanics.
Energy Search (TK1B #9): trainer effect stubbed.

Card text:
  - Search your deck for a basic Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="19a85642-d843-564c-85cd-e900d350de96",
    key="TK1B",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=9,
    set_code="TK1B",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
