"""STUB: effect not implemented — do not guess mechanics.
Lusamine (SM5 #153a): trainer effect stubbed.

Card text:
  - Put 2 in any combination of Supporter and Stadium cards from your discard pile into your hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="d8fddfb2-f391-52fa-b8bc-f39586a2e960",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lusamine.Name",
    display_name="Lusamine",
    searchable_by=["Lusamine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=178,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
