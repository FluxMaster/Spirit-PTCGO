"""STUB: effect not implemented — do not guess mechanics.
Sleep! (BASE5 #79): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, the Defending Pokémon is now Asleep.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c714eddf-86cb-5384-9b00-6e66f935d75d",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sleep.Name",
    display_name="Sleep!",
    searchable_by=["Sleep!", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=79,
    set_code="BASE5",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
