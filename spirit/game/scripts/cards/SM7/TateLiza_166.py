"""STUB: effect not implemented — do not guess mechanics.
Tate & Liza (SM7 #166): trainer effect stubbed.

Card text:
  - Choose 1:
• Shuffle your hand into your deck then draw 5 cards.
• Switch your Active Pokémon with 1 of your Benched Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="31fad7d0-76ee-5722-9734-f5dededecf30",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TateLiza.Name",
    display_name="Tate & Liza",
    searchable_by=["Tate & Liza", "Supporter"],
    subtypes=["Supporter"],
    collector_number=166,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
