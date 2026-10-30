"""STUB: effect not implemented — do not guess mechanics.
Team Aqua Technical Machine 01 (EX4 #79): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Pokémon that has Team Aqua in its name. That Pokémon may use this card's attack instead of its own. At the end of your turn, discard Team Aqua Technical Machine 01.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="be023159-3409-5271-8510-b4324b747af2",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaTechnicalMachine01.Name",
    display_name="Team Aqua Technical Machine 01",
    searchable_by=["Team Aqua Technical Machine 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=79,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
