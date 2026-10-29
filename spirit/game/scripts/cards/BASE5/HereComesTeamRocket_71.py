"""STUB: effect not implemented — do not guess mechanics.
Here Comes Team Rocket! (BASE5 #71): trainer effect stubbed.

Card text:
  - Each player plays with his or her Prize cards face up for the rest of the game.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b4d76d4d-5509-55a2-a6d1-5dd01c53ec69",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HereComesTeamRocket.Name",
    display_name="Here Comes Team Rocket!",
    searchable_by=["Here Comes Team Rocket!"],
    subtypes=[],
    collector_number=71,
    set_code="BASE5",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
