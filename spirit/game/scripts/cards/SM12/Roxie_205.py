"""STUB: effect not implemented — do not guess mechanics.
Roxie (SM12 #205): trainer effect stubbed.

Card text:
  - Discard up to 2 Pokémon that aren't Pokémon-GX or Pokémon-EX from your hand. Draw 3 cards for each card you discarded in this way.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="82b11538-fc23-5c88-a138-4813890384d9",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Roxie.Name",
    display_name="Roxie",
    searchable_by=["Roxie", "Supporter"],
    subtypes=["Supporter"],
    collector_number=205,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
