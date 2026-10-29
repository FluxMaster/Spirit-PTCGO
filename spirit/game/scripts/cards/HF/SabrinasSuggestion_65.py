"""STUB: effect not implemented — do not guess mechanics.
Sabrina's Suggestion (HF #65): trainer effect stubbed.

Card text:
  - Your opponent reveals their hand. You may choose a Supporter card you find there and use the effect of that card as the effect of this card.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="737c6c7d-51b9-5a96-902e-21fefb7b3984",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SabrinasSuggestion.Name",
    display_name="Sabrina's Suggestion",
    searchable_by=["Sabrina's Suggestion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=65,
    set_code="HF",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
