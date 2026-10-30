"""STUB: effect not implemented — do not guess mechanics.
Castaway (EX14 #72): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your deck for a Supporter card, a Pokémon Tool card, and a basic Energy card. Show them to your opponent, and put them into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="e13d3738-9e26-5020-810f-a901b29d6c2b",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Castaway.Name",
    display_name="Castaway",
    searchable_by=["Castaway", "Supporter"],
    subtypes=["Supporter"],
    collector_number=72,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
