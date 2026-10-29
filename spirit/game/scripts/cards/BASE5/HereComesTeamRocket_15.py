"""STUB: effect not implemented — do not guess mechanics.
Here Comes Team Rocket! (BASE5 #15): trainer effect stubbed.

Card text:
  - Each player plays with his or her Prize cards face up for the rest of the game.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c1823d45-d150-54bc-ac26-4dcedad8870d",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HereComesTeamRocket.Name",
    display_name="Here Comes Team Rocket!",
    searchable_by=["Here Comes Team Rocket!"],
    subtypes=[],
    collector_number=15,
    set_code="BASE5",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
