"""STUB: effect not implemented — do not guess mechanics.
Brock's Training (HF #55): trainer effect stubbed.

Card text:
  - Attach an Energy card from your hand to 1 of your Geodude, Graveler, Golem, Onix-GX, Cubone, Rhyhorn, Rhydon, or Sudowoodo.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="c9f5e4ac-36a4-5da9-acf1-d84198fbd72e",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksTraining.Name",
    display_name="Brock's Training",
    searchable_by=["Brock's Training", "Supporter"],
    subtypes=["Supporter"],
    collector_number=55,
    set_code="HF",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
