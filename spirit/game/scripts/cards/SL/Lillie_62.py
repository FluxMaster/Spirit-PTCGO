"""STUB: effect not implemented — do not guess mechanics.
Lillie (SL #62): trainer effect stubbed.

Card text:
  - Draw cards until you have 6 cards in your hand. If it's your first turn, draw cards until you have 8 cards in your hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="0bdec72a-fa96-5cd7-804e-f2acb9a0a479",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lillie.Name",
    display_name="Lillie",
    searchable_by=["Lillie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=62,
    set_code="SL",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
