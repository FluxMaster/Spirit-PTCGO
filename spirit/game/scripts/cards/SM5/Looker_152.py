"""STUB: effect not implemented — do not guess mechanics.
Looker (SM5 #152): trainer effect stubbed.

Card text:
  - Draw 3 cards from the bottom of your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="acf75027-5b78-53db-9607-969dc32f0e29",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Looker.Name",
    display_name="Looker",
    searchable_by=["Looker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=152,
    set_code="SM5",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
