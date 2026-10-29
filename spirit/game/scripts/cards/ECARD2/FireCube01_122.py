"""STUB: effect not implemented — do not guess mechanics.
Fire Cube 01 (ECARD2 #122): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Fire Pokémon in play. That Pokémon may use this card's attack instead of its own. At the end of your turn, discard Fire Cube 01.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="61024ef9-d0d7-542b-8ef8-041f77f2d6da",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FireCube01.Name",
    display_name="Fire Cube 01",
    searchable_by=["Fire Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=122,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
