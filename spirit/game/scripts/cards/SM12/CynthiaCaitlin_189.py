"""STUB: effect not implemented — do not guess mechanics.
Cynthia & Caitlin (SM12 #189): trainer effect stubbed.

Card text:
  - Put a Supporter card from your discard pile into your hand. You can't choose Cynthia & Caitlin or a card you discarded with the effect of this card.
  - When you play this card, you may discard another card from your hand. If you do, draw 3 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="e9c83471-65c5-5038-b053-46426391fc43",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CynthiaCaitlin.Name",
    display_name="Cynthia & Caitlin",
    searchable_by=["Cynthia & Caitlin", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=189,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
