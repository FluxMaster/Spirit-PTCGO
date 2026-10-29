"""STUB: effect not implemented — do not guess mechanics.
Bill's Analysis (SM9 #133): trainer effect stubbed.

Card text:
  - Look at the top 7 cards of your deck. You may reveal up to 2 Trainer cards you find there and put them into your hand. Shuffle the other cards back into your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="60363378-785f-56fb-9abe-55a1e4219a06",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsAnalysis.Name",
    display_name="Bill's Analysis",
    searchable_by=["Bill's Analysis", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="SM9",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
