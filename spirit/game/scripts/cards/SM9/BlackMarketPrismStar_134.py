"""STUB: effect not implemented — do not guess mechanics.
Black Market {*} (SM9 #134): trainer effect stubbed.

Card text:
  - When a Darkness Pokémon (yours or your opponent's) that has any Darkness Energy attached to it is Knocked Out by damage from an opponent's attack, that player takes 1 fewer Prize card.
  - Whenever any player plays an Item or Supporter card from their hand, prevent all effects of that card done to this Stadium card.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="8713634e-a490-56c7-b72f-a119019d7101",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlackMarketPrismStar.Name",
    display_name="Black Market {*}",
    searchable_by=["Black Market {*}", "Stadium", "Prism Star"],
    subtypes=["Stadium", "Prism Star"],
    collector_number=134,
    set_code="SM9",
    rarity=Rarities.Prism,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
