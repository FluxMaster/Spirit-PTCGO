"""STUB: effect not implemented — do not guess mechanics.
Roseanne's Research (POP8 #11): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your deck for up to 2 in any combination of Basic Pokémon and basic Energy cards, show them to your opponent, and put them into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="9c0d1a53-c416-502a-bec0-382d1b0e89a8",
    key="POP8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RoseannesResearch.Name",
    display_name="Roseanne's Research",
    searchable_by=["Roseanne's Research", "Supporter"],
    subtypes=["Supporter"],
    collector_number=11,
    set_code="POP8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
