"""STUB: effect not implemented — do not guess mechanics.
Morgan (SM9 #178): trainer effect stubbed.

Card text:
  - You can play this card only if you discard Dana, Evelyn, and Nita from your hand.
  - Look at the top 12 cards of your deck and attach any number of Energy cards you find there to your Pokémon in any way you like. Shuffle the other cards back into your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="b04c3743-5bbe-51cf-8a7a-da1c7b7beef7",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Morgan.Name",
    display_name="Morgan",
    searchable_by=["Morgan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=178,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
