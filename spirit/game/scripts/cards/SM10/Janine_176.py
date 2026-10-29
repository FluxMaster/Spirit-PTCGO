"""STUB: effect not implemented — do not guess mechanics.
Janine (SM10 #176): trainer effect stubbed.

Card text:
  - Look at the top 4 cards of your deck and put 2 of them into your hand. Shuffle the other cards back into your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="25628850-e253-5e25-a7d8-9282c01c76af",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Janine.Name",
    display_name="Janine",
    searchable_by=["Janine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=176,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
