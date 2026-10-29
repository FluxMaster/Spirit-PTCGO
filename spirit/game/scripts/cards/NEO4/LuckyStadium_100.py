"""STUB: effect not implemented — do not guess mechanics.
Lucky Stadium (NEO4 #100): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Once during each player's turn (before attacking), that player may flip a coin. If heads, that player draws a card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="53558e57-a4d1-5d49-bf3f-af31b2fa8a88",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LuckyStadium.Name",
    display_name="Lucky Stadium",
    searchable_by=["Lucky Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=100,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
