"""STUB: effect not implemented — do not guess mechanics.
Energy Stadium (NEO4 #99): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Once during each player's turn (before attacking), that player may flip a coin. If heads, that player puts a basic Energy card from his or her discard pile into his or her hand.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="02b0c11b-06d6-5bc7-9ee6-e920ed4bbda5",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyStadium.Name",
    display_name="Energy Stadium",
    searchable_by=["Energy Stadium", "Stadium"],
    subtypes=["Stadium"],
    collector_number=99,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
