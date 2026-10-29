"""STUB: effect not implemented — do not guess mechanics.
Sabrina's Suggestion (SM9 #154): trainer effect stubbed.

Card text:
  - Your opponent reveals their hand. You may choose a Supporter card you find there and use the effect of that card as the effect of this card.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="ea70ea85-89a6-5b5b-87c8-55c229b32ed7",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SabrinasSuggestion.Name",
    display_name="Sabrina's Suggestion",
    searchable_by=["Sabrina's Suggestion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=154,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
