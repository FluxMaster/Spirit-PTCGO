"""STUB: effect not implemented — do not guess mechanics.
Underground Expedition (SM7 #150): trainer effect stubbed.

Card text:
  - Look at the bottom 4 cards of your deck and put 2 of them into your hand. Put the other cards back on the bottom of your deck in any order.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="8e14809a-ab53-554a-8897-7c48c6b2b730",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UndergroundExpedition.Name",
    display_name="Underground Expedition",
    searchable_by=["Underground Expedition", "Supporter"],
    subtypes=["Supporter"],
    collector_number=150,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
