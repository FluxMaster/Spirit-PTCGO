"""STUB: effect not implemented — do not guess mechanics.
Sabrina's Suggestion (SM9 #181): trainer effect stubbed.

Card text:
  - Your opponent reveals their hand. You may choose a Supporter card you find there and use the effect of that card as the effect of this card.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="cb183046-4137-5ec9-b50a-2d557e444d09",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SabrinasSuggestion.Name",
    display_name="Sabrina's Suggestion",
    searchable_by=["Sabrina's Suggestion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=181,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
