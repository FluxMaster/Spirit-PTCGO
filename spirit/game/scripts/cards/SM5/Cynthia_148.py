"""STUB: effect not implemented — do not guess mechanics.
Cynthia (SM5 #148): trainer effect stubbed.

Card text:
  - Shuffle your hand into your deck. Then, draw 6 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="8ea804bd-9540-5de4-940d-39094d485f4b",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cynthia.Name",
    display_name="Cynthia",
    searchable_by=["Cynthia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=148,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
