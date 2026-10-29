"""STUB: effect not implemented — do not guess mechanics.
Celadon City Gym (GYM1 #107): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - During each player's turn, that player may choose to discard an Energy card attached to 1 of his or her Pokémon with Erika in its name. If that player does so, that Pokémon is no longer Asleep, Confused, Paralyzed, or Poisoned.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="332ba831-6589-57d8-b8ce-a98c30f95580",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CeladonCityGym.Name",
    display_name="Celadon City Gym",
    searchable_by=["Celadon City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=107,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
