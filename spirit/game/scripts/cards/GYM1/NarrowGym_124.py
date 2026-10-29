"""STUB: effect not implemented — do not guess mechanics.
Narrow Gym (GYM1 #124): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - No player may have more than 4 Pokémon on his or her Bench. When this card is played, if a player has 5 Pokémon on his or her Bench, that player chooses 1 of them and returns it and all cards attached to it to his or her hand. (If both players have to return a Pokémon, your opponent returns a Pokémon first.)
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="ca0234f1-1d6c-5034-8e96-3b1c06d62344",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NarrowGym.Name",
    display_name="Narrow Gym",
    searchable_by=["Narrow Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=124,
    set_code="GYM1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
