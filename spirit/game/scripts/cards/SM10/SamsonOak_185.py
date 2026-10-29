"""STUB: effect not implemented — do not guess mechanics.
Samson Oak (SM10 #185): trainer effect stubbed.

Card text:
  - Draw 2 cards. If both Active Pokémon are the same type, draw 2 more cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="23e345e9-9e38-5bdd-8e07-46ddf59d6d1e",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SamsonOak.Name",
    display_name="Samson Oak",
    searchable_by=["Samson Oak", "Supporter"],
    subtypes=["Supporter"],
    collector_number=185,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
