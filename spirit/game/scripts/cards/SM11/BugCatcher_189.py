"""STUB: effect not implemented — do not guess mechanics.
Bug Catcher (SM11 #189): trainer effect stubbed.

Card text:
  - Draw 2 cards. Flip a coin. If heads, draw 2 more cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="824cd96a-2209-5375-8ffb-c0694a5407ba",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BugCatcher.Name",
    display_name="Bug Catcher",
    searchable_by=["Bug Catcher", "Supporter"],
    subtypes=["Supporter"],
    collector_number=189,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
