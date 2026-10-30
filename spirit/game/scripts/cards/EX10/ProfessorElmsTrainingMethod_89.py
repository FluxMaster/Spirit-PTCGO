"""STUB: effect not implemented — do not guess mechanics.
Professor Elm's Training Method (EX10 #89): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your deck for an Evolution card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="ca1075c3-c906-5bc9-ba32-0707c6636521",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorElmsTrainingMethod.Name",
    display_name="Professor Elm's Training Method",
    searchable_by=["Professor Elm's Training Method", "Supporter"],
    subtypes=["Supporter"],
    collector_number=89,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
