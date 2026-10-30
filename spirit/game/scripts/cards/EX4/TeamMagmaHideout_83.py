"""STUB: effect not implemented — do not guess mechanics.
Team Magma Hideout (EX4 #83): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Whenever any player plays a Basic Pokémon that doesn't have Team Magma in its name from his or her hand, that player puts 1 damage counter on that Pokémon.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="9c01768b-b7a2-5259-a978-6545d4298e00",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaHideout.Name",
    display_name="Team Magma Hideout",
    searchable_by=["Team Magma Hideout", "Stadium"],
    subtypes=["Stadium"],
    collector_number=83,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
