"""STUB: effect not implemented — do not guess mechanics.
Power Tree (EX12 #76): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Once during each player's turn, if the player has no Special Energy cards in his or her discard pile, that player searches his or her discard pile for a basic Energy card, show it to the opponent, and put it into his or her hand.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="062a4d57-2b14-50d6-a998-4207aa9cd370",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowerTree.Name",
    display_name="Power Tree",
    searchable_by=["Power Tree", "Stadium"],
    subtypes=["Stadium"],
    collector_number=76,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
