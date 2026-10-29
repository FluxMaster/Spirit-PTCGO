"""STUB: effect not implemented — do not guess mechanics.
Forest Guardian (ECARD2 #123): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Shuffle your deck. Then, look at the top 7 cards of your deck. Choose 1 of those cards and put it into your hand. Shuffle the rest into your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="7b04c584-4115-5f15-a26d-bca587ffea4e",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ForestGuardian.Name",
    display_name="Forest Guardian",
    searchable_by=["Forest Guardian", "Supporter"],
    subtypes=["Supporter"],
    collector_number=123,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
