"""STUB: effect not implemented — do not guess mechanics.
Lance {*} (DM #61): trainer effect stubbed.

Card text:
  - You can play this card only if 1 of your Pokémon was Knocked Out during your opponent's last turn.
  - Search your deck for up to 2 Dragon Pokémon and put them onto your Bench. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
  - ◇ (Prism Star) Rule: You can't have more than 1 ◇ card with the same name in your deck. If a ◇ card would go to the discard pile, put it in the Lost Zone instead.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="e3ebff2a-f53c-550d-afcf-caf8d079d6ab",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LancePrismStar.Name",
    display_name="Lance {*}",
    searchable_by=["Lance {*}", "Supporter", "Prism Star"],
    subtypes=["Supporter", "Prism Star"],
    collector_number=61,
    set_code="DM",
    rarity=Rarities.Prism,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
