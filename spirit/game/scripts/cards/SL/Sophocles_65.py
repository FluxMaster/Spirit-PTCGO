"""STUB: effect not implemented — do not guess mechanics.
Sophocles (SL #65): trainer effect stubbed.

Card text:
  - Discard 2 cards from your hand. If you do, draw 4 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="121d7b5b-2df7-54ef-b717-d18bb0806535",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sophocles.Name",
    display_name="Sophocles",
    searchable_by=["Sophocles", "Supporter"],
    subtypes=["Supporter"],
    collector_number=65,
    set_code="SL",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
