"""STUB: effect not implemented — do not guess mechanics.
Lysandre {*} (SM6 #110): trainer effect stubbed.

Card text:
  - For each of your Fire Pokémon in play, put a card from your opponent's discard pile in the Lost Zone.
  - You may play only 1 Supporter card during your turn (before your attack).
  - ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="89bf6e51-6769-5f5b-b1b4-f0aec5c9ea0c",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LysandrePrismStar.Name",
    display_name="Lysandre {*}",
    searchable_by=["Lysandre {*}", "Supporter", "Prism Star"],
    subtypes=["Supporter", "Prism Star"],
    collector_number=110,
    set_code="SM6",
    rarity=Rarities.Prism,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
