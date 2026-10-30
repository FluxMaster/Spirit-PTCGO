"""STUB: effect not implemented — do not guess mechanics.
Team Aqua Schemer (EX4 #69): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Discard any 1 Pokémon from your hand. Then draw 3 cards. If you discarded a Pokémon with Team Aqua in its name, draw 4 cards instead.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="755aee45-0ba8-5bab-bc47-f3faf4638fec",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaSchemer.Name",
    display_name="Team Aqua Schemer",
    searchable_by=["Team Aqua Schemer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=69,
    set_code="EX4",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
