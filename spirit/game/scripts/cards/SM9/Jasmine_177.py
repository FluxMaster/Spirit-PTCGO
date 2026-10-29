"""STUB: effect not implemented — do not guess mechanics.
Jasmine (SM9 #177): trainer effect stubbed.

Card text:
  - Search your deck for a Metal Pokémon, reveal it, and put it into your hand. If you go second and it's your first turn, search for 5 Metal Pokémon instead of 1. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="cab8c0f0-2b8d-5bf7-8940-bc54a2b14b24",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Jasmine.Name",
    display_name="Jasmine",
    searchable_by=["Jasmine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=177,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
