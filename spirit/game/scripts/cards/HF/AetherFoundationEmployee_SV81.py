"""STUB: effect not implemented — do not guess mechanics.
Aether Foundation Employee (HF #SV81): trainer effect stubbed.

Card text:
  - Put 3 Pokémon that have "Alolan" in their names from your discard pile into your hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="e0372110-c3c6-5305-a6ca-fdfeeee25b82",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AetherFoundationEmployee.Name",
    display_name="Aether Foundation Employee",
    searchable_by=["Aether Foundation Employee", "Supporter"],
    subtypes=["Supporter"],
    collector_number=150,
    set_code="HF",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
