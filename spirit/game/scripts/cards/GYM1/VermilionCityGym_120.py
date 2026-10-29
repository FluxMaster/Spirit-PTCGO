"""STUB: effect not implemented — do not guess mechanics.
Vermilion City Gym (GYM1 #120): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Whenever a player attacks with a Pokémon with Lt. Surge in its name, he or she may flip a coin. If heads, and if that Pokémon's attack does damage to the Defending Pokémon (after applying Weakness and Resistance), that attack does 10 more damage to the Defending Pokémon. If tails, the attacking Pokémon does 10 damage to itself in addition to whatever its attack usually does.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="0760beea-88de-58bf-9526-3ebe4198398f",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VermilionCityGym.Name",
    display_name="Vermilion City Gym",
    searchable_by=["Vermilion City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=120,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
