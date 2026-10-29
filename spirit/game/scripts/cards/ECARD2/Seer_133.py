"""STUB: effect not implemented — do not guess mechanics.
Seer (ECARD2 #133): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Look at the top 6 cards of your deck. Take all Basic Energy cards you find there, show them to your opponent, and then put them into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="024715b9-f516-53ea-a1f1-42e05ad073af",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Seer.Name",
    display_name="Seer",
    searchable_by=["Seer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
