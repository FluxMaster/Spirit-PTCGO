"""STUB: effect not implemented — do not guess mechanics.
Lisia (SM7 #164): trainer effect stubbed.

Card text:
  - Search your deck for up to 2 ◇ (Prism Star) cards, reveal them, and put them into your hand. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="505bf65f-28dc-5209-87ed-3c0abc7ebfbf",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lisia.Name",
    display_name="Lisia",
    searchable_by=["Lisia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=164,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
