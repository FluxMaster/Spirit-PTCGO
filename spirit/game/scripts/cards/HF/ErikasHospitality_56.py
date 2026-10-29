"""STUB: effect not implemented — do not guess mechanics.
Erika's Hospitality (HF #56): trainer effect stubbed.

Card text:
  - You can play this card only if you have 4 or fewer other cards in your hand.
  - Draw a card for each of your opponent's Pokémon in play.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="85226b04-9e88-5572-b57a-3e3da3f50665",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ErikasHospitality.Name",
    display_name="Erika's Hospitality",
    searchable_by=["Erika's Hospitality", "Supporter"],
    subtypes=["Supporter"],
    collector_number=56,
    set_code="HF",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
