"""STUB: effect not implemented — do not guess mechanics.
Broken Ground Gym (NEO4 #92): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Each player pays Colorless more to retreat a Baby Pokémon or Basic Pokémon.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="f33cb209-4280-5b4f-87e8-5ff656b7feb4",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrokenGroundGym.Name",
    display_name="Broken Ground Gym",
    searchable_by=["Broken Ground Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=92,
    set_code="NEO4",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
