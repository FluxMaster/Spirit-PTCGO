"""STUB: effect not implemented — do not guess mechanics.
Professor Elm's Training Method (EX15 #79): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your deck for an Evolution card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="66aafb48-0f1b-5a93-94ed-dabde6734c7c",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorElmsTrainingMethod.Name",
    display_name="Professor Elm's Training Method",
    searchable_by=["Professor Elm's Training Method", "Supporter"],
    subtypes=["Supporter"],
    collector_number=79,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
