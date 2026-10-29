"""STUB: effect not implemented — do not guess mechanics.
Lanette's Net Search (EX2 #87): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your deck for up to 3 different types of Basic Pokémon cards (excluding Baby Pokémon), show them to your opponent, and put them into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="bcb48bd8-729f-576e-bd58-e1f97cb26749",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LanettesNetSearch.Name",
    display_name="Lanette's Net Search",
    searchable_by=["Lanette's Net Search", "Supporter"],
    subtypes=["Supporter"],
    collector_number=87,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
