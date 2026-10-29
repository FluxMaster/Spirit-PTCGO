"""STUB: effect not implemented — do not guess mechanics.
Trash Exchange (GYM1 #126): trainer effect stubbed.

Card text:
  - Count the number of cards in your discard pile and shuffle them into your deck. Then discard that many cards from the top of your deck.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="6b1ca45d-4d01-5dbe-98b3-f8694877ec7d",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TrashExchange.Name",
    display_name="Trash Exchange",
    searchable_by=["Trash Exchange"],
    subtypes=[],
    collector_number=126,
    set_code="GYM1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
