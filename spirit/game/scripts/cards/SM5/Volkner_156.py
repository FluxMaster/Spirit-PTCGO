"""STUB: effect not implemented — do not guess mechanics.
Volkner (SM5 #156): trainer effect stubbed.

Card text:
  - Search your deck for an Item card and a Lightning Energy card, reveal them, and put them into your hand. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="a96066ea-4d1f-5671-acd4-712921ce6500",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Volkner.Name",
    display_name="Volkner",
    searchable_by=["Volkner", "Supporter"],
    subtypes=["Supporter"],
    collector_number=156,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
