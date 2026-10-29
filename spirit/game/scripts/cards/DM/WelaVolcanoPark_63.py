"""STUB: effect not implemented — do not guess mechanics.
Wela Volcano Park (DM #63): trainer effect stubbed.

Card text:
  - Whenever a player flips a coin for the Special Condition Burned between turns, that Special Condition isn't removed even if the result is heads.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="dd8595de-b606-5d37-94d8-ce36fbed6758",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WelaVolcanoPark.Name",
    display_name="Wela Volcano Park",
    searchable_by=["Wela Volcano Park", "Stadium"],
    subtypes=["Stadium"],
    collector_number=63,
    set_code="DM",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
