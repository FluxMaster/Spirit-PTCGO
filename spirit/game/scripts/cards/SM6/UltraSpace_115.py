"""STUB: effect not implemented — do not guess mechanics.
Ultra Space (SM6 #115): trainer effect stubbed.

Card text:
  - Once during each player's turn, that player may search their deck for an Ultra Beast card, reveal it, put it into their hand, and shuffle their deck.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="275ec1de-d82c-5643-8416-eb4529477822",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraSpace.Name",
    display_name="Ultra Space",
    searchable_by=["Ultra Space", "Stadium"],
    subtypes=["Stadium"],
    collector_number=115,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
