"""STUB: effect not implemented — do not guess mechanics.
Team Magma Conspirator (EX4 #82): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your deck for up to 2 in any combination of Basic Pokémon with Team Magma in its name and basic Energy cards, show them to your opponent, and put them into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="57e43eca-5888-5767-8c3f-692192d3b576",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaConspirator.Name",
    display_name="Team Magma Conspirator",
    searchable_by=["Team Magma Conspirator", "Supporter"],
    subtypes=["Supporter"],
    collector_number=82,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
