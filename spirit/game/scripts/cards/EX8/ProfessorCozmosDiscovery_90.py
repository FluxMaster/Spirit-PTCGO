"""STUB: effect not implemented — do not guess mechanics.
Professor Cozmo's Discovery (EX8 #90): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Flip a coin. If heads, draw the bottom 3 cards of your deck. If tails, draw the top 2 cards of your deck.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="b9aaee14-e388-5c7b-8376-c5529b761d6f",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorCozmosDiscovery.Name",
    display_name="Professor Cozmo's Discovery",
    searchable_by=["Professor Cozmo's Discovery", "Supporter"],
    subtypes=["Supporter"],
    collector_number=90,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
