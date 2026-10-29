"""STUB: effect not implemented — do not guess mechanics.
Volkner (SM5 #135): trainer effect stubbed.

Card text:
  - Search your deck for an Item card and a Lightning Energy card, reveal them, and put them into your hand. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="03be53aa-c19f-5a03-b6cf-13c6de2496f4",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Volkner.Name",
    display_name="Volkner",
    searchable_by=["Volkner", "Supporter"],
    subtypes=["Supporter"],
    collector_number=135,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
