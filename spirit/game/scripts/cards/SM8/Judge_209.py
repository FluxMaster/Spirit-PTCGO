"""STUB: effect not implemented — do not guess mechanics.
Judge (SM8 #209): trainer effect stubbed.

Card text:
  - Each player shuffles their hand into their deck and draws 4 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="96ab001e-a1e2-51da-8492-0b80104abea5",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Judge.Name",
    display_name="Judge",
    searchable_by=["Judge", "Supporter"],
    subtypes=["Supporter"],
    collector_number=209,
    set_code="SM8",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
