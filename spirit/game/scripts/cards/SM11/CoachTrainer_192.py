"""STUB: effect not implemented — do not guess mechanics.
Coach Trainer (SM11 #192): trainer effect stubbed.

Card text:
  - Draw 2 cards. If your Active Pokémon is a TAG TEAM Pokémon, draw 2 more cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="0697d68b-a1f8-5182-bc75-290b5d6428f6",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CoachTrainer.Name",
    display_name="Coach Trainer",
    searchable_by=["Coach Trainer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=192,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
