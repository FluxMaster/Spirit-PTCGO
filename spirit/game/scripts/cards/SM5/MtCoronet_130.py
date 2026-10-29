"""STUB: effect not implemented — do not guess mechanics.
Mt. Coronet (SM5 #130): trainer effect stubbed.

Card text:
  - Once during each player's turn, that player may put 2 Metal Energy cards from their discard pile into their hand.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="a5e0c70a-ae34-542b-bbab-8a774b4b9348",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MtCoronet.Name",
    display_name="Mt. Coronet",
    searchable_by=["Mt. Coronet", "Stadium"],
    subtypes=["Stadium"],
    collector_number=130,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
