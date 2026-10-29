"""STUB: effect not implemented — do not guess mechanics.
Cynthia (HF #SV82): trainer effect stubbed.

Card text:
  - Shuffle your hand into your deck. Then, draw 6 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="68a06f33-f721-5452-a4c5-0bb6e64f675e",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cynthia.Name",
    display_name="Cynthia",
    searchable_by=["Cynthia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=151,
    set_code="HF",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
