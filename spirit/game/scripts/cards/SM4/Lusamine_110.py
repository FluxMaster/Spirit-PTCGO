"""STUB: effect not implemented — do not guess mechanics.
Lusamine (SM4 #110): trainer effect stubbed.

Card text:
  - Put 2 in any combination of Supporter and Stadium cards from your discard pile into your hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="a7f7f22d-a109-5513-b901-2238d08d02b6",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lusamine.Name",
    display_name="Lusamine",
    searchable_by=["Lusamine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=110,
    set_code="SM4",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
