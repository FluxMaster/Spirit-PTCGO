"""STUB: effect not implemented — do not guess mechanics.
Lass (BASE1 #75): trainer effect stubbed.

Card text:
  - You and your opponent show each other your hands, then shuffle all the Trainer cards from your hands into your decks.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="da0753bd-4246-5ff7-b80b-1581a9594eeb",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lass.Name",
    display_name="Lass",
    searchable_by=["Lass"],
    subtypes=[],
    collector_number=75,
    set_code="BASE1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
