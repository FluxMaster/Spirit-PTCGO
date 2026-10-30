"""STUB: effect not implemented — do not guess mechanics.
Team Aqua Hideout (EX4 #78): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Each Pokémon that does not have Team Aqua in its name pays Colorless more to retreat.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="0a0b1ff6-c5b0-5cee-b5a1-f2a785a8a4da",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaHideout.Name",
    display_name="Team Aqua Hideout",
    searchable_by=["Team Aqua Hideout", "Stadium"],
    subtypes=["Stadium"],
    collector_number=78,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
