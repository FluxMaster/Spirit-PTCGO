"""STUB: effect not implemented — do not guess mechanics.
Gambler (BASE3 #60): trainer effect stubbed.

Card text:
  - Shuffle your hand into your deck. Flip a coin. If heads, draw 8 cards. If tails, draw 1 card.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="f7849688-e0a5-50cb-bbaf-58f734588de4",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Gambler.Name",
    display_name="Gambler",
    searchable_by=["Gambler"],
    subtypes=[],
    collector_number=60,
    set_code="BASE3",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
