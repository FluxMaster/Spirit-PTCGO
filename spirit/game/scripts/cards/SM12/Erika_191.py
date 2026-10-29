"""STUB: effect not implemented — do not guess mechanics.
Erika (SM12 #191): trainer effect stubbed.

Card text:
  - Each player may draw up to 3 cards. You draw first.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="300486c6-3ec5-5def-85b2-26398321ac90",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Erika.Name",
    display_name="Erika",
    searchable_by=["Erika", "Supporter"],
    subtypes=["Supporter"],
    collector_number=191,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
