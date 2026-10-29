"""STUB: effect not implemented — do not guess mechanics.
Resistance Gym (GYM2 #109): trainer effect stubbed.

Card text:
  - This card stays in play after being played. Discard this card if another Stadium card comes into play.
  - Each Pokémon's Resistance is reduced by 20. (If a Pokémon's Resistance is -30, it becomes -10.)
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="3414be12-a0f0-59ad-9cdd-a7ec9a2d91b6",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ResistanceGym.Name",
    display_name="Resistance Gym",
    searchable_by=["Resistance Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=109,
    set_code="GYM2",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
