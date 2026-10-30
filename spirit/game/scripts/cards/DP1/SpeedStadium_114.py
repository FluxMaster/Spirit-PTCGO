"""STUB: effect not implemented — do not guess mechanics.
Speed Stadium (DP1 #114): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Once during each player's turn, the player may flip a coin until he or she gets tails. For each heads, that player draws a card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="ccc3ee1d-ce38-59cd-a7e3-cd22c9467086",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpeedStadium.Name",
    display_name="Speed Stadium",
    searchable_by=["Speed Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=114,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
