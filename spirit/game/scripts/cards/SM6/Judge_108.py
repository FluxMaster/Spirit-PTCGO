"""STUB: effect not implemented — do not guess mechanics.
Judge (SM6 #108): trainer effect stubbed.

Card text:
  - Each player shuffles their hand into their deck and draws 4 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="844bb265-b3fe-51da-a98b-c43786c85389",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Judge.Name",
    display_name="Judge",
    searchable_by=["Judge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=108,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
