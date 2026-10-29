"""STUB: effect not implemented — do not guess mechanics.
Hiker (HF #SV85): trainer effect stubbed.

Card text:
  - Look at the top 5 cards of either player's deck and choose 1 of them. That player shuffles the other cards back into their deck. Then, put the card you chose on top of that deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="6ec9927a-a69f-59e2-871a-6e7277eeb200",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hiker.Name",
    display_name="Hiker",
    searchable_by=["Hiker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=154,
    set_code="HF",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
