"""STUB: effect not implemented — do not guess mechanics.
Whitney (SM8 #193): trainer effect stubbed.

Card text:
  - Draw a card. Then, draw 2 cards for each other Whitney in your discard pile.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="cf211409-753a-597d-8e7c-4dd579656076",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Whitney.Name",
    display_name="Whitney",
    searchable_by=["Whitney", "Supporter"],
    subtypes=["Supporter"],
    collector_number=193,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
