"""STUB: effect not implemented — do not guess mechanics.
No Removal Gym (GYM1 #103): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - A player must discard 2 cards from his or her hand in order to play an Energy Removal or Super Energy Removal card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="e6c8a31a-483c-5f9b-968c-9ee76b7c4710",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NoRemovalGym.Name",
    display_name="No Removal Gym",
    searchable_by=["No Removal Gym", "Stadium"],
    subtypes=["Stadium"],
    collector_number=103,
    set_code="GYM1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
