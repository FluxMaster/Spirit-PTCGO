"""STUB: effect not implemented — do not guess mechanics.
Lillie (SM5 #151): trainer effect stubbed.

Card text:
  - Draw cards until you have 6 cards in your hand. If it's your first turn, draw cards until you have 8 cards in your hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="b3b4ff7f-79e7-5f12-8cd6-16476a12de20",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lillie.Name",
    display_name="Lillie",
    searchable_by=["Lillie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=151,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
