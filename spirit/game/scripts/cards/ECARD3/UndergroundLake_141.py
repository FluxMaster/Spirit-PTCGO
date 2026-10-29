"""STUB: effect not implemented — do not guess mechanics.
Underground Lake (ECARD3 #141): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Once during each player's turn, that player may put an Omanyte or a Kabuto card from his or her discard pile onto his or her Bench. (Cards put on the Bench this way are considered Basic Pokémon.)
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="cef622e7-dd42-5c7c-9221-1a22335e1ec0",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UndergroundLake.Name",
    display_name="Underground Lake",
    searchable_by=["Underground Lake", "Stadium"],
    subtypes=["Stadium"],
    collector_number=141,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
