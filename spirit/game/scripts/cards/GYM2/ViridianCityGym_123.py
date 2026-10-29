"""STUB: effect not implemented — do not guess mechanics.
Viridian City Gym (GYM2 #123): trainer effect stubbed.

Card text:
  - This card stays in play after being played. Discard this card if another Stadium card comes into play.
  - Whenever a Pokémon with Giovanni in its name evolves, its owner removes 2 damage counters from that Pokémon (or 1 if it only has 1).
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="ebf437b8-1aed-58a3-a919-6dcf794937d8",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ViridianCityGym.Name",
    display_name="Viridian City Gym",
    searchable_by=["Viridian City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=123,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
