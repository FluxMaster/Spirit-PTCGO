"""STUB: effect not implemented — do not guess mechanics.
Lisia (SM7 #137): trainer effect stubbed.

Card text:
  - Search your deck for up to 2 ◇ (Prism Star) cards, reveal them, and put them into your hand. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="170666de-07f5-5edf-9be1-f084cf6c13d1",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lisia.Name",
    display_name="Lisia",
    searchable_by=["Lisia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=137,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
