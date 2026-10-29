"""STUB: effect not implemented — do not guess mechanics.
Gladion (SM4 #95): trainer effect stubbed.

Card text:
  - Look at your face-down Prize cards and put 1 of them into your hand. Then, shuffle this Gladion into your remaining Prize cards and put them back face down. If you didn't play this Gladion from your hand, it does nothing.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="b43d09c8-ab22-5d3b-af7f-6f3481608951",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Gladion.Name",
    display_name="Gladion",
    searchable_by=["Gladion", "Supporter"],
    subtypes=["Supporter"],
    collector_number=95,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
