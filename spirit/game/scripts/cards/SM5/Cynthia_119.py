"""STUB: effect not implemented — do not guess mechanics.
Cynthia (SM5 #119): trainer effect stubbed.

Card text:
  - Shuffle your hand into your deck. Then, draw 6 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="c996e0ff-54cd-5315-bc79-5af76413ce68",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Cynthia.Name",
    display_name="Cynthia",
    searchable_by=["Cynthia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=119,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
