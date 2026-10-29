"""STUB: effect not implemented — do not guess mechanics.
Olivia (SM4 #111): trainer effect stubbed.

Card text:
  - Search your deck for up to 2 Pokémon-GX, reveal them, and put them into your hand. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="8311aa5c-45d0-58a7-8194-c16ff88f14a6",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Olivia.Name",
    display_name="Olivia",
    searchable_by=["Olivia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=111,
    set_code="SM4",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
