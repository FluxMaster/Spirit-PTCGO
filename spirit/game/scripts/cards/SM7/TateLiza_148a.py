"""STUB: effect not implemented — do not guess mechanics.
Tate & Liza (SM7 #148a): trainer effect stubbed.

Card text:
  - Choose 1:
• Shuffle your hand into your deck then draw 5 cards.
• Switch your Active Pokémon with 1 of your Benched Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="efd86a39-acdd-5424-b099-5221856a75c3",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TateLiza.Name",
    display_name="Tate & Liza",
    searchable_by=["Tate & Liza", "Supporter"],
    subtypes=["Supporter"],
    collector_number=186,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
