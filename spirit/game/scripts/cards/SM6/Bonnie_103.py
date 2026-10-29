"""STUB: effect not implemented — do not guess mechanics.
Bonnie (SM6 #103): trainer effect stubbed.

Card text:
  - You can play this card only if there is any Stadium card in play.
  - Discard that Stadium card. During this turn, your Zygarde-GX can use its GX attack even if you have used your GX attack.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="60d0a3af-5b9c-5c67-8aba-bff059e62847",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Bonnie.Name",
    display_name="Bonnie",
    searchable_by=["Bonnie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=103,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
