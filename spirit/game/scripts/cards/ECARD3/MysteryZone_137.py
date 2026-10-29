"""STUB: effect not implemented — do not guess mechanics.
Mystery Zone (ECARD3 #137): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Once during each player's turn (before he or she attacks), if that player has an Evolution card in his or her hand, he or she may search his or her deck for a basic Energy card, show it to his or her opponent, and put it into his or her hand. Then that player chooses an Evolution card from his or her hand, shows it to his or her opponent, and puts it into his or her deck. That player shuffles his or her deck afterward.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="7547734d-3a2d-5dff-9ca6-be96b8ce13ad",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteryZone.Name",
    display_name="Mystery Zone",
    searchable_by=["Mystery Zone", "Stadium"],
    subtypes=["Stadium"],
    collector_number=137,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
