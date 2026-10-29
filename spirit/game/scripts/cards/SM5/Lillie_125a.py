"""STUB: effect not implemented — do not guess mechanics.
Lillie (SM5 #125a): trainer effect stubbed.

Card text:
  - Draw cards until you have 6 cards in your hand. If it's your first turn, draw cards until you have 8 cards in your hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="27d7e715-a52b-5196-83a2-63e4b0a10361",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lillie.Name",
    display_name="Lillie",
    searchable_by=["Lillie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=176,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
