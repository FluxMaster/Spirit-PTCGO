"""STUB: effect not implemented — do not guess mechanics.
Cerulean City Gym (GYM1 #108): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Each player pays Colorless less to retreat his or her Pokémon if it has Misty in its name.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="b06ff56d-2204-5fec-84a3-4398d36e4545",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CeruleanCityGym.Name",
    display_name="Cerulean City Gym",
    searchable_by=["Cerulean City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=108,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
