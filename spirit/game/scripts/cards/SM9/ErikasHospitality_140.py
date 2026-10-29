"""STUB: effect not implemented — do not guess mechanics.
Erika's Hospitality (SM9 #140): trainer effect stubbed.

Card text:
  - You can play this card only if you have 4 or fewer other cards in your hand.
  - Draw a card for each of your opponent's Pokémon in play.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="f7eb4870-efd0-5bc8-8935-276dd4c90248",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ErikasHospitality.Name",
    display_name="Erika's Hospitality",
    searchable_by=["Erika's Hospitality", "Supporter"],
    subtypes=["Supporter"],
    collector_number=140,
    set_code="SM9",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
