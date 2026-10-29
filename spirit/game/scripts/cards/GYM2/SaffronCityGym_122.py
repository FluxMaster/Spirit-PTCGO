"""STUB: effect not implemented — do not guess mechanics.
Saffron City Gym (GYM2 #122): trainer effect stubbed.

Card text:
  - This card stays in play after being played. Discard this card if another Stadium card comes into play.
  - As often as each player like during his or her turn (before attacking), that player may return 1 basic Energy card attached to 1 of his or her Pokémon with Sabrina in its name to his or her hand.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="43d43b08-9d0f-5e3a-b4b0-68ad948ec074",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SaffronCityGym.Name",
    display_name="Saffron City Gym",
    searchable_by=["Saffron City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=122,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
