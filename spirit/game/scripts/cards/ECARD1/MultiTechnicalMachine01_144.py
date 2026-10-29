"""STUB: effect not implemented — do not guess mechanics.
Multi Technical Machine 01 (ECARD1 #144): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Pokémon in play. That Pokémon may use this card's attack instead of its own. At the end of your turn, discard Multi Technical Machine 01.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="66be2075-cf24-5927-8a3c-4417587c8c4c",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MultiTechnicalMachine01.Name",
    display_name="Multi Technical Machine 01",
    searchable_by=["Multi Technical Machine 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=144,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
