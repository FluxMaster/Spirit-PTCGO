"""STUB: effect not implemented — do not guess mechanics.
Crasher Wake (SM6 #104): trainer effect stubbed.

Card text:
  - Discard 2 Water Energy cards from your hand. If you do, search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="33528646-2ab5-5dab-91c5-b0f7610b8d5c",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrasherWake.Name",
    display_name="Crasher Wake",
    searchable_by=["Crasher Wake", "Supporter"],
    subtypes=["Supporter"],
    collector_number=104,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
