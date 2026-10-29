"""STUB: effect not implemented — do not guess mechanics.
Lavender Town (SM9 #147): trainer effect stubbed.

Card text:
  - Once during each player's turn, that player may have their opponent reveal their hand.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="6a6dbfa1-4f6d-5511-82d2-6a709d43bb5d",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LavenderTown.Name",
    display_name="Lavender Town",
    searchable_by=["Lavender Town", "Stadium"],
    subtypes=["Stadium"],
    collector_number=147,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
