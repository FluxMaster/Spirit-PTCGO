"""STUB: effect not implemented — do not guess mechanics.
Bonnie (SM6 #128): trainer effect stubbed.

Card text:
  - You can play this card only if there is any Stadium card in play.
  - Discard that Stadium card. During this turn, your Zygarde-GX can use its GX attack even if you have used your GX attack.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="6bdc2fce-76e7-5f93-b359-01371a8198be",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bonnie.Name",
    display_name="Bonnie",
    searchable_by=["Bonnie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=128,
    set_code="SM6",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
