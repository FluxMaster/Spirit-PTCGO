"""STUB: effect not implemented — do not guess mechanics.
Gardenia (SM5 #124): trainer effect stubbed.

Card text:
  - Heal 80 damage from 1 of your Pokémon that has any Grass Energy attached to it.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="54942e2f-c703-50ee-b634-7b23d5a46a45",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Gardenia.Name",
    display_name="Gardenia",
    searchable_by=["Gardenia", "Supporter"],
    subtypes=["Supporter"],
    collector_number=124,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
