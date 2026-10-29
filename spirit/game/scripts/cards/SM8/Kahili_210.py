"""STUB: effect not implemented — do not guess mechanics.
Kahili (SM8 #210): trainer effect stubbed.

Card text:
  - Draw 2 cards. Then, flip a coin. If heads, if you played this Kahili from your hand, put this card into your hand instead of the discard pile. If you have no cards in your deck, you can't play this card.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="b7f0356f-1b0d-52b8-ad1b-d1333a43d713",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kahili.Name",
    display_name="Kahili",
    searchable_by=["Kahili", "Supporter"],
    subtypes=["Supporter"],
    collector_number=210,
    set_code="SM8",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
