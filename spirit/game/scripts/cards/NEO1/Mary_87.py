"""STUB: effect not implemented — do not guess mechanics.
Mary (NEO1 #87): trainer effect stubbed.

Card text:
  - Draw 2 cards. Then, shuffle 2 cards from your hand into your deck.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="0c3ceeb5-261d-59f2-b81a-a9ba9351e29d",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mary.Name",
    display_name="Mary",
    searchable_by=["Mary"],
    subtypes=[],
    collector_number=87,
    set_code="NEO1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
