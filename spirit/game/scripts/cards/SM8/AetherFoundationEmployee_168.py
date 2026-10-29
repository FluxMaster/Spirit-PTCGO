"""STUB: effect not implemented — do not guess mechanics.
Aether Foundation Employee (SM8 #168): trainer effect stubbed.

Card text:
  - Put 3 Pokémon that have "Alolan" in their names from your discard pile into your hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="eed448cd-793c-57e1-9f9c-7409c6b27e7d",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AetherFoundationEmployee.Name",
    display_name="Aether Foundation Employee",
    searchable_by=["Aether Foundation Employee", "Supporter"],
    subtypes=["Supporter"],
    collector_number=168,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
