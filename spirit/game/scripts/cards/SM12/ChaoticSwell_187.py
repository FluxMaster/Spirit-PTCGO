"""STUB: effect not implemented — do not guess mechanics.
Chaotic Swell (SM12 #187): trainer effect stubbed.

Card text:
  - Whenever either player plays a Stadium card from their hand, discard that Stadium card after discarding this one. (The new Stadium card has no effect.)
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="53ff5d70-7635-5aad-b190-be61c579151d",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ChaoticSwell.Name",
    display_name="Chaotic Swell",
    searchable_by=["Chaotic Swell", "Stadium"],
    subtypes=["Stadium"],
    collector_number=187,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
