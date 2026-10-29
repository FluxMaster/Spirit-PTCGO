"""STUB: effect not implemented — do not guess mechanics.
Dana (SM9 #173): trainer effect stubbed.

Card text:
  - You can play this card only if your opponent's Active Pokémon is a Stage 2 Pokémon.
  - Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="c30e707e-dfed-5d15-a697-d00df9cf6e0a",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Dana.Name",
    display_name="Dana",
    searchable_by=["Dana", "Supporter"],
    subtypes=["Supporter"],
    collector_number=173,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
