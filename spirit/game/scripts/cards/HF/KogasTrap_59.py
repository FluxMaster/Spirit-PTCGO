"""STUB: effect not implemented — do not guess mechanics.
Koga's Trap (HF #59): trainer effect stubbed.

Card text:
  - Your opponent's Active Pokémon is now Confused and Poisoned.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="e9112bd6-8e01-5f66-b1c7-caed7b635293",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.KogasTrap.Name",
    display_name="Koga's Trap",
    searchable_by=["Koga's Trap", "Supporter"],
    subtypes=["Supporter"],
    collector_number=59,
    set_code="HF",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
