"""STUB: effect not implemented — do not guess mechanics.
Lass (BASE4 #104): trainer effect stubbed.

Card text:
  - You and your opponent show each other your hands, then shuffle all the Trainer cards from your hands into your decks.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="6b1a01aa-1f51-57ae-90df-798afdd9c40c",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lass.Name",
    display_name="Lass",
    searchable_by=["Lass"],
    subtypes=[],
    collector_number=104,
    set_code="BASE4",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
