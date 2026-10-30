"""STUB: effect not implemented — do not guess mechanics.
Team Magma Schemer (EX4 #70): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Discard any 1 Pokémon from your hand. Then draw 3 cards. If you discarded a Pokémon with Team Magma in its name, draw 4 cards instead.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="7afae935-e342-5191-80bf-91948c09f657",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaSchemer.Name",
    display_name="Team Magma Schemer",
    searchable_by=["Team Magma Schemer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=70,
    set_code="EX4",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
