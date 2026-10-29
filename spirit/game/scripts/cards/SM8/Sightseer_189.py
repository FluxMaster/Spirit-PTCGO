"""STUB: effect not implemented — do not guess mechanics.
Sightseer (SM8 #189): trainer effect stubbed.

Card text:
  - You may discard any number of cards from your hand. Then, draw cards until you have 5 cards in your hand. If you can't draw any cards in this way, you can't play this card.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="ed9c6b83-624d-5988-8e78-05bc8da629d2",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sightseer.Name",
    display_name="Sightseer",
    searchable_by=["Sightseer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=189,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
