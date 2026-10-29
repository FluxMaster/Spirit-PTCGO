"""STUB: effect not implemented — do not guess mechanics.
Bellelba & Brycen-Man (SM12 #186): trainer effect stubbed.

Card text:
  - Discard 3 cards from the top of each player's deck.
  - When you play this card, you may discard 3 other cards from your hand. If you do, each player discards their Benched Pokémon until they have 3 Benched Pokémon. Your opponent discards first.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="138ffcaa-5146-5450-8849-d9e4afb25a84",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BellelbaBrycenMan.Name",
    display_name="Bellelba & Brycen-Man",
    searchable_by=["Bellelba & Brycen-Man", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=186,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
