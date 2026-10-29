"""STUB: effect not implemented — do not guess mechanics.
Lana (SM3 #117): trainer effect stubbed.

Card text:
  - Heal 50 damage from each of your Pokémon that has any Water Energy attached to it.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="08d08d68-ebe6-54a0-b651-9978fd2adb7d",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lana.Name",
    display_name="Lana",
    searchable_by=["Lana", "Supporter"],
    subtypes=["Supporter"],
    collector_number=117,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
