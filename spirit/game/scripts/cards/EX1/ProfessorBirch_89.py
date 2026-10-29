"""STUB: effect not implemented — do not guess mechanics.
Professor Birch (EX1 #89): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Draw cards from your deck until you have 6 cards in your hand.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="bfd15a05-86eb-5f2c-9c21-71dfad37d917",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorBirch.Name",
    display_name="Professor Birch",
    searchable_by=["Professor Birch", "Supporter"],
    subtypes=["Supporter"],
    collector_number=89,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
