"""STUB: effect not implemented — do not guess mechanics.
Thunder Mountain {*} (SM8 #191): trainer effect stubbed.

Card text:
  - The attacks of Lightning Pokémon (both yours and your opponent's) cost Lightning less.
  - Whenever any player plays an Item or Supporter card from their hand, prevent all effects of that card done to this Stadium card.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="1485ad3a-47aa-5606-bf5c-8f4df4389ca2",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ThunderMountainPrismStar.Name",
    display_name="Thunder Mountain {*}",
    searchable_by=["Thunder Mountain {*}", "Stadium", "Prism Star"],
    subtypes=["Stadium", "Prism Star"],
    collector_number=191,
    set_code="SM8",
    rarity=Rarities.Prism,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
