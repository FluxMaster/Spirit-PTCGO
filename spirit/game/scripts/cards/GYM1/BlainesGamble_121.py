"""STUB: effect not implemented — do not guess mechanics.
Blaine's Gamble (GYM1 #121): trainer effect stubbed.

Card text:
  - Discard any number of other cards from your hand, then flip a coin. If heads, draw twice that many cards.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="6323b3d5-1cea-545a-bf23-cd0b376a5082",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesGamble.Name",
    display_name="Blaine's Gamble",
    searchable_by=["Blaine's Gamble"],
    subtypes=[],
    collector_number=121,
    set_code="GYM1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
