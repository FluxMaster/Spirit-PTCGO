"""STUB: effect not implemented — do not guess mechanics.
Lana (SM5 #150): trainer effect stubbed.

Card text:
  - Heal 50 damage from each of your Pokémon that has any Water Energy attached to it.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="26e358be-9513-5754-b607-ed8ce789deaf",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lana.Name",
    display_name="Lana",
    searchable_by=["Lana", "Supporter"],
    subtypes=["Supporter"],
    collector_number=150,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
