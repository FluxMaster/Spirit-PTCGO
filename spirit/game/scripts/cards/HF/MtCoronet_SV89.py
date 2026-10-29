"""STUB: effect not implemented — do not guess mechanics.
Mt. Coronet (HF #SV89): trainer effect stubbed.

Card text:
  - Once during each player's turn, that player may put 2 Metal Energy cards from their discard pile into their hand.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="7149eb36-4b7f-5cae-aef6-7507bda35ab6",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MtCoronet.Name",
    display_name="Mt. Coronet",
    searchable_by=["Mt. Coronet", "Stadium"],
    subtypes=["Stadium"],
    collector_number=158,
    set_code="HF",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
