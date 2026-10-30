"""STUB: effect not implemented — do not guess mechanics.
Rocket's Tricky Gym (EX7 #90): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Each Pokémon with Dark or Rocket's in its name (both yours and your opponent's) can use attacks on this card instead of its own.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="38056161-8551-5f40-9ccc-966f315acdf6",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsTrickyGym.Name",
    display_name="Rocket's Tricky Gym",
    searchable_by=["Rocket's Tricky Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=90,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
