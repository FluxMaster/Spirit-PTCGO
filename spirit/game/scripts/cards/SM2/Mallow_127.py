"""STUB: effect not implemented — do not guess mechanics.
Mallow (SM2 #127): trainer effect stubbed.

Card text:
  - Search your deck for 2 cards, shuffle your deck, and put those cards on top of your deck in any order.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="999af1e2-d460-56b7-b812-18dcfed40236",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mallow.Name",
    display_name="Mallow",
    searchable_by=["Mallow", "Supporter"],
    subtypes=["Supporter"],
    collector_number=127,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
