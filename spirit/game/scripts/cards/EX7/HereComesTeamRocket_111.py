"""STUB: effect not implemented — do not guess mechanics.
Here Comes Team Rocket! (EX7 #111): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Each player plays with his or her Prize cards face up for the rest of the game.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="d8b31bbe-ade3-5ff4-a0b2-7f556a108a34",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HereComesTeamRocket.Name",
    display_name="Here Comes Team Rocket!",
    searchable_by=["Here Comes Team Rocket!", "Supporter"],
    subtypes=["Supporter"],
    collector_number=111,
    set_code="EX7",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
