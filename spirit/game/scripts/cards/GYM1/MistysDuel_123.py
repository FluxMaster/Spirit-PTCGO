"""STUB: effect not implemented — do not guess mechanics.
Misty's Duel (GYM1 #123): trainer effect stubbed.

Card text:
  - You and your opponent play a game of Rock-Paper-Scissors. The winner shuffles his or her hand into his or her deck and draws a new hand of 5 cards. (If you don't know how to play Rock-Paper-Scissors, flip a coin to decide who's the winner.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="f619ee51-f7cb-5140-aadc-aae64672190b",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysDuel.Name",
    display_name="Misty's Duel",
    searchable_by=["Misty's Duel"],
    subtypes=[],
    collector_number=123,
    set_code="GYM1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
