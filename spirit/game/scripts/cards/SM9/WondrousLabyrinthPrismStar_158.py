"""STUB: effect not implemented — do not guess mechanics.
Wondrous Labyrinth {*} (SM9 #158): trainer effect stubbed.

Card text:
  - The attacks of non-Fairy Pokémon (both yours and your opponent's) cost Colorless more.
  - Whenever any player plays an Item or Supporter card from their hand, prevent all effects of that card done to this Stadium card.
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="d51677c0-4efd-53b4-b1fb-50b59414cb3e",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WondrousLabyrinthPrismStar.Name",
    display_name="Wondrous Labyrinth {*}",
    searchable_by=["Wondrous Labyrinth {*}", "Stadium", "Prism Star"],
    subtypes=["Stadium", "Prism Star"],
    collector_number=158,
    set_code="SM9",
    rarity=Rarities.Prism,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
