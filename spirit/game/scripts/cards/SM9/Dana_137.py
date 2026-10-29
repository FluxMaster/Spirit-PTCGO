"""STUB: effect not implemented — do not guess mechanics.
Dana (SM9 #137): trainer effect stubbed.

Card text:
  - You can play this card only if your opponent's Active Pokémon is a Stage 2 Pokémon.
  - Search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="f7b0941e-0a4d-5f1f-a46f-78a5f6b1467e",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Dana.Name",
    display_name="Dana",
    searchable_by=["Dana", "Supporter"],
    subtypes=["Supporter"],
    collector_number=137,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
