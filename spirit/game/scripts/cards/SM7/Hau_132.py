"""STUB: effect not implemented — do not guess mechanics.
Hau (SM7 #132): trainer effect stubbed.

Card text:
  - Draw 3 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="1ab3de67-7cea-5db7-b176-8758dfae4ff7",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Hau.Name",
    display_name="Hau",
    searchable_by=["Hau", "Supporter"],
    subtypes=["Supporter"],
    collector_number=132,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
