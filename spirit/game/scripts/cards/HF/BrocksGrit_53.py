"""STUB: effect not implemented — do not guess mechanics.
Brock's Grit (HF #53): trainer effect stubbed.

Card text:
  - Shuffle 6 in any combination of Pokémon and basic Energy cards from your discard pile into your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="9a9ff7e9-7328-5ce7-b42d-a99100c931d3",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksGrit.Name",
    display_name="Brock's Grit",
    searchable_by=["Brock's Grit", "Supporter"],
    subtypes=["Supporter"],
    collector_number=53,
    set_code="HF",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
