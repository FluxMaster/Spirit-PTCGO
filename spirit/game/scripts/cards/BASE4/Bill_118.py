"""STUB: effect not implemented — do not guess mechanics.
Bill (BASE4 #118): trainer effect stubbed.

Card text:
  - Draw 2 cards.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="87d14847-b7fb-5bac-a173-f4333188f321",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bill.Name",
    display_name="Bill",
    searchable_by=["Bill"],
    subtypes=[],
    collector_number=118,
    set_code="BASE4",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
