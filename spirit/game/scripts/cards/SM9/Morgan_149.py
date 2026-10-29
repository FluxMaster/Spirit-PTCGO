"""STUB: effect not implemented — do not guess mechanics.
Morgan (SM9 #149): trainer effect stubbed.

Card text:
  - You can play this card only if you discard Dana, Evelyn, and Nita from your hand.
  - Look at the top 12 cards of your deck and attach any number of Energy cards you find there to your Pokémon in any way you like. Shuffle the other cards back into your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="a7ad922d-1bd6-5fcd-b378-830c4699c2af",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Morgan.Name",
    display_name="Morgan",
    searchable_by=["Morgan", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
