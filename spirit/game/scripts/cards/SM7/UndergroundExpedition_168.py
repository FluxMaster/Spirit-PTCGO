"""STUB: effect not implemented — do not guess mechanics.
Underground Expedition (SM7 #168): trainer effect stubbed.

Card text:
  - Look at the bottom 4 cards of your deck and put 2 of them into your hand. Put the other cards back on the bottom of your deck in any order.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="50cfd7d5-0839-5841-b2aa-3702bb9caac1",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UndergroundExpedition.Name",
    display_name="Underground Expedition",
    searchable_by=["Underground Expedition", "Supporter"],
    subtypes=["Supporter"],
    collector_number=168,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
