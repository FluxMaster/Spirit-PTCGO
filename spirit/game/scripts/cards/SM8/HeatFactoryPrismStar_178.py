"""STUB: effect not implemented — do not guess mechanics.
Heat Factory {*} (SM8 #178): trainer effect stubbed.

Card text:
  - Once during each player's turn, that player may discard a Fire Energy card from their hand. If they do, they draw 3 cards.
  - Whenever any player plays an Item or Supporter card from their hand, prevent all effects of that card done to this Stadium card.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="e1bd8637-68e3-5fa6-a2e6-bc09bae61021",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HeatFactoryPrismStar.Name",
    display_name="Heat Factory {*}",
    searchable_by=["Heat Factory {*}", "Stadium", "Prism Star"],
    subtypes=["Stadium", "Prism Star"],
    collector_number=178,
    set_code="SM8",
    rarity=Rarities.Prism,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
