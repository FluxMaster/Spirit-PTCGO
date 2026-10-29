"""STUB: effect not implemented — do not guess mechanics.
Rocket's Minefield Gym (GYM2 #119): trainer effect stubbed.

Card text:
  - This card stays in play after being played. Discard this card if another Stadium card comes into play.
  - Whenever a player puts a Basic Pokémon onto his or her Bench from his or her hand, he or she flips a coin. If tails, put damage counters on that Pokémon.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="001174e4-1a40-5fb7-a678-f8555a7adb78",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsMinefieldGym.Name",
    display_name="Rocket's Minefield Gym",
    searchable_by=["Rocket's Minefield Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=119,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
