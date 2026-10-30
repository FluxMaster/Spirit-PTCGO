"""STUB: effect not implemented — do not guess mechanics.
Team Aqua Conspirator (EX4 #77): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your deck for up to 2 in any combination of Basic Pokémon with Team Aqua in its name and basic Energy cards, show them to your opponent, and put them into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="5b9c5358-b321-50c1-81ce-e7b2dfac9360",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaConspirator.Name",
    display_name="Team Aqua Conspirator",
    searchable_by=["Team Aqua Conspirator", "Supporter"],
    subtypes=["Supporter"],
    collector_number=77,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
