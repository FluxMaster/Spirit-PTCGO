"""STUB: effect not implemented — do not guess mechanics.
Prof. Oak's Research (EX6 #98): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Shuffle your hand into your deck, then draw 5 cards.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="55151212-9092-5d92-ab11-d9606709cc4c",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfOaksResearch.Name",
    display_name="Prof. Oak's Research",
    searchable_by=["Prof. Oak's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=98,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
