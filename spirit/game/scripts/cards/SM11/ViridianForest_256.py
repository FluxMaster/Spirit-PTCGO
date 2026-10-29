"""STUB: effect not implemented — do not guess mechanics.
Viridian Forest (SM11 #256): trainer effect stubbed.

Card text:
  - Once during each player's turn, that player may discard a card from their hand. If they do, that player searches their deck for a basic Energy card, reveals it, and puts it into their hand. Then, that player shuffles their deck.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="097a3578-7537-511d-b4ac-5993524d7b23",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ViridianForest.Name",
    display_name="Viridian Forest",
    searchable_by=["Viridian Forest", "Stadium"],
    subtypes=["Stadium"],
    collector_number=256,
    set_code="SM11",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
