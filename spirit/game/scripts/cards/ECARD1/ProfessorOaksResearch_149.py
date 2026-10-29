"""STUB: effect not implemented — do not guess mechanics.
Professor Oak's Research (ECARD1 #149): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Shuffle your hand into your deck, then draw 5 cards.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="8ed08e76-4e36-5cc5-a903-30b4ec0760ba",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksResearch.Name",
    display_name="Professor Oak's Research",
    searchable_by=["Professor Oak's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
