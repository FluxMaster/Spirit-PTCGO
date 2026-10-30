"""STUB: effect not implemented — do not guess mechanics.
Team Magma Technical Machine 01 (EX4 #84): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Pokémon that has Team Magma in its name. That Pokémon may use this card's attack instead of its own. At the end of your turn, discard Team Magma Technical Machine 01.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="fe0aa9f0-e8a4-59f6-8566-4911efc060f5",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaTechnicalMachine01.Name",
    display_name="Team Magma Technical Machine 01",
    searchable_by=["Team Magma Technical Machine 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=84,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
