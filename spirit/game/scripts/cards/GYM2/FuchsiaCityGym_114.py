"""STUB: effect not implemented — do not guess mechanics.
Fuchsia City Gym (GYM2 #114): trainer effect stubbed.

Card text:
  - This card stays in play after being played. Discard this card if another Stadium card comes into play.
  - Once during each player's turn (before attacking), that player may flip a coin. If heads, that player may shuffle 1 of his or her Pokémon in play with Koga in its name and any cards attached to it into his or her deck.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="4115c0f1-efc5-53b0-b8a4-4b043ae81c7c",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FuchsiaCityGym.Name",
    display_name="Fuchsia City Gym",
    searchable_by=["Fuchsia City Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=114,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
