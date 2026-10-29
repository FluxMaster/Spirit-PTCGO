"""STUB: effect not implemented — do not guess mechanics.
Clay (SM12 #188): trainer effect stubbed.

Card text:
  - Discard the top 7 cards of your deck. If any of those cards are Item cards, put them into your hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="5b24b989-b802-57e1-b96b-4912c7be9eb4",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Clay.Name",
    display_name="Clay",
    searchable_by=["Clay", "Supporter"],
    subtypes=["Supporter"],
    collector_number=188,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
