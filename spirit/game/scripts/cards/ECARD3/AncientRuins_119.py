"""STUB: effect not implemented — do not guess mechanics.
Ancient Ruins (ECARD3 #119): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Once during each player's turn (before he or she attacks), if he or she has not played a Supporter card, that player may reveal his or her hand to his or her opponent. If that player reveals his or her hand and there is no Supporter card there, that player draws a card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="ab4d0d31-b831-544a-a999-cc68262693ca",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientRuins.Name",
    display_name="Ancient Ruins",
    searchable_by=["Ancient Ruins", "Stadium"],
    subtypes=["Stadium"],
    collector_number=119,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
