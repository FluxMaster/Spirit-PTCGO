"""STUB: effect not implemented — do not guess mechanics.
Professor Cozmo's Discovery (TK2A #10): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Flip a coin. If heads, draw the bottom 3 cards of your deck. If tails, draw the top 2 cards of your deck.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="52a71ff9-ebde-56a4-ae5b-665536d8b0f3",
    key="TK2A",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorCozmosDiscovery.Name",
    display_name="Professor Cozmo's Discovery",
    searchable_by=["Professor Cozmo's Discovery", "Supporter"],
    subtypes=["Supporter"],
    collector_number=10,
    set_code="TK2A",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
