"""STUB: effect not implemented — do not guess mechanics.
Coach Trainer (SM11 #233): trainer effect stubbed.

Card text:
  - Draw 2 cards. If your Active Pokémon is a TAG TEAM Pokémon, draw 2 more cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="14d502f5-c4be-50ca-b46e-90648b7d90b7",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CoachTrainer.Name",
    display_name="Coach Trainer",
    searchable_by=["Coach Trainer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=233,
    set_code="SM11",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
