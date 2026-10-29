"""STUB: effect not implemented — do not guess mechanics.
Copycat (SM7 #127): trainer effect stubbed.

Card text:
  - Shuffle your hand into your deck. Then, draw a card for each card in your opponent's hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="7ba71e38-118d-5a54-b9f5-7c81dff6dcc5",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Copycat.Name",
    display_name="Copycat",
    searchable_by=["Copycat", "Supporter"],
    subtypes=["Supporter"],
    collector_number=127,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
