"""STUB: effect not implemented — do not guess mechanics.
Professor Oak's Research (EX15 #80): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Shuffle your hand into your deck, then draw 5 cards.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="d5d9ad67-c5e3-5947-81af-2dadf8e1c5ac",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksResearch.Name",
    display_name="Professor Oak's Research",
    searchable_by=["Professor Oak's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=80,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
