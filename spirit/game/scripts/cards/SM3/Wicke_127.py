"""STUB: effect not implemented — do not guess mechanics.
Wicke (SM3 #127): trainer effect stubbed.

Card text:
  - Each player counts the cards in their hand, shuffles those cards into their deck, then draws that many cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="e63bb517-bde7-5919-a3b4-d5f6b02fceeb",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Wicke.Name",
    display_name="Wicke",
    searchable_by=["Wicke", "Supporter"],
    subtypes=["Supporter"],
    collector_number=127,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
