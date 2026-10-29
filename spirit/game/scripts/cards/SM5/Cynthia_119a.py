"""STUB: effect not implemented — do not guess mechanics.
Cynthia (SM5 #119a): trainer effect stubbed.

Card text:
  - Shuffle your hand into your deck. Then, draw 6 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="64b75b5f-83c1-573e-865f-8cf13b9f667e",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cynthia.Name",
    display_name="Cynthia",
    searchable_by=["Cynthia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=174,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
