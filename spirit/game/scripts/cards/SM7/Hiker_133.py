"""STUB: effect not implemented — do not guess mechanics.
Hiker (SM7 #133): trainer effect stubbed.

Card text:
  - Look at the top 5 cards of either player's deck and choose 1 of them. That player shuffles the other cards back into their deck. Then, put the card you chose on top of that deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="5c0b86c8-f5b9-54aa-9692-2488c3ecc3c8",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hiker.Name",
    display_name="Hiker",
    searchable_by=["Hiker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
