"""STUB: effect not implemented — do not guess mechanics.
TV Reporter (SM7 #167): trainer effect stubbed.

Card text:
  - Draw 3 cards. Then, discard a card from your hand. If you have no cards in your deck, you can't play this card.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="9e8e4f82-9912-5d22-8c89-2bdec7a1f04f",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TVReporter.Name",
    display_name="TV Reporter",
    searchable_by=["TV Reporter", "Supporter"],
    subtypes=["Supporter"],
    collector_number=167,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
