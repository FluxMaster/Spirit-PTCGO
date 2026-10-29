"""STUB: effect not implemented — do not guess mechanics.
Lusamine {*} (SM8 #182): trainer effect stubbed.

Card text:
  - You can play this card only if your opponent has exactly 3 Prize cards remaining.
  - Prevent all damage done to your Ultra Beasts by attacks during your opponent's next turn.
  - You may play only 1 Supporter card during your turn (before your attack).
  - ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="7b69fe43-db66-5d21-ac4c-038ba1cb2d18",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LusaminePrismStar.Name",
    display_name="Lusamine {*}",
    searchable_by=["Lusamine {*}", "Supporter", "Prism Star"],
    subtypes=["Supporter", "Prism Star"],
    collector_number=182,
    set_code="SM8",
    rarity=Rarities.Prism,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
