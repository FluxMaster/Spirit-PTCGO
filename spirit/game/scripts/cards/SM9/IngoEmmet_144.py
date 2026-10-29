"""STUB: effect not implemented — do not guess mechanics.
Ingo & Emmet (SM9 #144): trainer effect stubbed.

Card text:
  - Look at the top card of your deck, and then choose 1:
• Discard your hand and draw 5 cards.
• Discard your hand and draw 5 cards from the bottom of your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="0f5a1f20-cd44-578b-9b9d-a1c8481903b5",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IngoEmmet.Name",
    display_name="Ingo & Emmet",
    searchable_by=["Ingo & Emmet", "Supporter"],
    subtypes=["Supporter"],
    collector_number=144,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
