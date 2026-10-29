"""STUB: effect not implemented — do not guess mechanics.
Recycle (BASE3 #61): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, put a card in your discard pile on top of your deck.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="dc249005-d213-5514-864f-90704c0ca770",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Recycle.Name",
    display_name="Recycle",
    searchable_by=["Recycle"],
    subtypes=[],
    collector_number=61,
    set_code="BASE3",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
