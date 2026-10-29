"""STUB: effect not implemented — do not guess mechanics.
Apricorn Maker (SM7 #161): trainer effect stubbed.

Card text:
  - Search your deck for up to 2 Item cards that have the word "Ball" in their name, reveal them, and put them into your hand. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="22e510d3-8464-514d-8f9d-626260a00a63",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ApricornMaker.Name",
    display_name="Apricorn Maker",
    searchable_by=["Apricorn Maker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=161,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
