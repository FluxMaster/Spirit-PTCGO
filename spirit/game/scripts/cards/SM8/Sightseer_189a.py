"""STUB: effect not implemented — do not guess mechanics.
Sightseer (SM8 #189a): trainer effect stubbed.

Card text:
  - You may discard any number of cards from your hand. Then, draw cards until you have 5 cards in your hand. If you can't draw any cards in this way, you can't play this card.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="3f36dbdb-a788-5301-a1e9-f71da182ea1e",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sightseer.Name",
    display_name="Sightseer",
    searchable_by=["Sightseer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=240,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
