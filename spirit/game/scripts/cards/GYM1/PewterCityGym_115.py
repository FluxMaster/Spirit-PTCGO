"""STUB: effect not implemented — do not guess mechanics.
Pewter City Gym (GYM1 #115): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Don't apply Resistance to any attacks made by Pokémon with Brock in their names.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="deb0626a-251f-5250-8e39-76750dd7d088",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PewterCityGym.Name",
    display_name="Pewter City Gym",
    searchable_by=["Pewter City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=115,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
