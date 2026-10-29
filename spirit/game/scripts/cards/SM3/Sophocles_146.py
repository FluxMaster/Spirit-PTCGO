"""STUB: effect not implemented — do not guess mechanics.
Sophocles (SM3 #146): trainer effect stubbed.

Card text:
  - Discard 2 cards from your hand. If you do, draw 4 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="3f41a19d-8ebf-5746-bb30-ee4ec05fc216",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sophocles.Name",
    display_name="Sophocles",
    searchable_by=["Sophocles", "Supporter"],
    subtypes=["Supporter"],
    collector_number=146,
    set_code="SM3",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
