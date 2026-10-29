"""STUB: effect not implemented — do not guess mechanics.
Mars (SM5 #128): trainer effect stubbed.

Card text:
  - Draw 2 cards. If you do, discard a random card from your opponent's hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="995329f5-c227-5f4b-b551-b7e25bef0985",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mars.Name",
    display_name="Mars",
    searchable_by=["Mars", "Supporter"],
    subtypes=["Supporter"],
    collector_number=128,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
