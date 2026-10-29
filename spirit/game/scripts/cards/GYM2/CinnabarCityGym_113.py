"""STUB: effect not implemented — do not guess mechanics.
Cinnabar City Gym (GYM2 #113): trainer effect stubbed.

Card text:
  - This card stays in play after being played. Discard this card if another Stadium card comes into play.
  - Ignore Weakness when a Water Pokémon does damage to a Pokémon with Blaine in its name.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="c6be19f3-4b3c-5811-a8c8-ebda04595583",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CinnabarCityGym.Name",
    display_name="Cinnabar City Gym",
    searchable_by=["Cinnabar City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=113,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
