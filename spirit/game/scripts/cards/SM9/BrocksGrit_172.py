"""STUB: effect not implemented — do not guess mechanics.
Brock's Grit (SM9 #172): trainer effect stubbed.

Card text:
  - Shuffle 6 in any combination of Pokémon and basic Energy cards from your discard pile into your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="76a5e6ca-7405-5fcb-9e4d-29d4da35c255",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksGrit.Name",
    display_name="Brock's Grit",
    searchable_by=["Brock's Grit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=172,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
