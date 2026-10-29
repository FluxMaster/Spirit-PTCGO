"""STUB: effect not implemented — do not guess mechanics.
Water Cube 01 (ECARD2 #140): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Water Pokémon in play. That Pokémon may use this card's attack instead of its own. At the end of your turn, discard Water Cube 01.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="acac7eec-f073-54fa-b4e7-67d254f65d31",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WaterCube01.Name",
    display_name="Water Cube 01",
    searchable_by=["Water Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=140,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
