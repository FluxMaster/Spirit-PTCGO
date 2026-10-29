"""STUB: effect not implemented — do not guess mechanics.
Sabrina & Brycen (Promo_SM #SM246): trainer effect stubbed.

Card text:
  - Search your deck for up to 2 basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.
  - When you play this card, you may discard 5 other cards from your hand. If you do, you may also search for up to 3 Pokémon of different types in this way.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="54a7c071-836c-55d3-840c-e06814f569c5",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SabrinaBrycen.Name",
    display_name="Sabrina & Brycen",
    searchable_by=["Sabrina & Brycen", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=246,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
