"""STUB: effect not implemented — do not guess mechanics.
Sabrina's Gaze (GYM1 #125): trainer effect stubbed.

Card text:
  - Each player shuffles his or her hand into his or her deck and draws a new hand of the same number of cards.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="a3834562-2c17-5e08-a84f-ad8648b9f17b",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SabrinasGaze.Name",
    display_name="Sabrina's Gaze",
    searchable_by=["Sabrina's Gaze"],
    subtypes=[],
    collector_number=125,
    set_code="GYM1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
