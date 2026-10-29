"""STUB: effect not implemented — do not guess mechanics.
Whitney (SM8 #214): trainer effect stubbed.

Card text:
  - Draw a card. Then, draw 2 cards for each other Whitney in your discard pile.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="8c5c5238-a591-51ef-97ce-959a0faadc5a",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Whitney.Name",
    display_name="Whitney",
    searchable_by=["Whitney", "Supporter"],
    subtypes=["Supporter"],
    collector_number=214,
    set_code="SM8",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
