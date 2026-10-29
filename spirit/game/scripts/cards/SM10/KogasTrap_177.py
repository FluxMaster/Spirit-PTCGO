"""STUB: effect not implemented — do not guess mechanics.
Koga's Trap (SM10 #177): trainer effect stubbed.

Card text:
  - Your opponent's Active Pokémon is now Confused and Poisoned.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="fe0d8b54-8354-5e00-b2bc-14ee250a1450",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.KogasTrap.Name",
    display_name="Koga's Trap",
    searchable_by=["Koga's Trap", "Supporter"],
    subtypes=["Supporter"],
    collector_number=177,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
