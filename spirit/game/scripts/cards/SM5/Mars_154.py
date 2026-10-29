"""STUB: effect not implemented — do not guess mechanics.
Mars (SM5 #154): trainer effect stubbed.

Card text:
  - Draw 2 cards. If you do, discard a random card from your opponent's hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="2b5f706d-5c17-508e-b7c9-48a40b8f2162",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mars.Name",
    display_name="Mars",
    searchable_by=["Mars", "Supporter"],
    subtypes=["Supporter"],
    collector_number=154,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
