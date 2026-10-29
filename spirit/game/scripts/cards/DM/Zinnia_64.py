"""STUB: effect not implemented — do not guess mechanics.
Zinnia (DM #64): trainer effect stubbed.

Card text:
  - You can play this card only if 1 of your Pokémon was Knocked Out during your opponent's last turn.
  - Attach up to 2 basic Energy cards from your hand to 1 of your Dragon Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="1fc05985-a25a-5825-a3eb-e83c8ae36363",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Zinnia.Name",
    display_name="Zinnia",
    searchable_by=["Zinnia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=64,
    set_code="DM",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
