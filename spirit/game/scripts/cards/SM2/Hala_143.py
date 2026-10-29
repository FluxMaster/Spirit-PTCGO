"""STUB: effect not implemented — do not guess mechanics.
Hala (SM2 #143): trainer effect stubbed.

Card text:
  - Shuffle your hand into your deck. If you have used your GX attack, draw 7 cards. If not, draw 4 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="f3084b97-94c7-581c-8d61-9cf6f4fca24a",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hala.Name",
    display_name="Hala",
    searchable_by=["Hala", "Supporter"],
    subtypes=["Supporter"],
    collector_number=143,
    set_code="SM2",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
