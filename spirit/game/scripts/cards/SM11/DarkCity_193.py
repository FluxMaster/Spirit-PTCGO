"""STUB: effect not implemented — do not guess mechanics.
Dark City (SM11 #193): trainer effect stubbed.

Card text:
  - Basic Darkness Pokémon in play (both yours and your opponent's) have no Retreat Cost.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="514ebc7f-bc7d-5240-ae25-3bfb27344360",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DarkCity.Name",
    display_name="Dark City",
    searchable_by=["Dark City", "Stadium"],
    subtypes=["Stadium"],
    collector_number=193,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
