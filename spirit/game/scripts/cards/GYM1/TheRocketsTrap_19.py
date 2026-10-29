"""STUB: effect not implemented — do not guess mechanics.
The Rocket's Trap (GYM1 #19): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, choose up to 3 cards at random from your opponent's hand (don't look at them). Your opponent shuffles those cards into his or her deck.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="1edcdd0e-f7ce-5a0d-8e37-2d7fc33d7699",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TheRocketsTrap.Name",
    display_name="The Rocket's Trap",
    searchable_by=["The Rocket's Trap"],
    subtypes=[],
    collector_number=19,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
