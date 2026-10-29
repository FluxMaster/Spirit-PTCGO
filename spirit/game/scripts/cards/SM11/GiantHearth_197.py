"""STUB: effect not implemented — do not guess mechanics.
Giant Hearth (SM11 #197): trainer effect stubbed.

Card text:
  - Once during each player's turn, that player may discard a card from their hand. If they do, that player searches their deck for up to 2 Fire Energy cards, reveals them, and puts them into their hand. Then, that player shuffles their deck.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="dc4ddfa1-db4b-5d2d-859f-bf1af01f7e9d",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiantHearth.Name",
    display_name="Giant Hearth",
    searchable_by=["Giant Hearth", "Stadium"],
    subtypes=["Stadium"],
    collector_number=197,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
