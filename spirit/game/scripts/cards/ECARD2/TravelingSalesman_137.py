"""STUB: effect not implemented — do not guess mechanics.
Traveling Salesman (ECARD2 #137): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your deck for up to 2 Technical Machine and/or Pokémon Tool cards, show them to your opponent, and then put them into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="c0fe7623-f237-5205-a417-776add2aaa3b",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TravelingSalesman.Name",
    display_name="Traveling Salesman",
    searchable_by=["Traveling Salesman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=137,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
