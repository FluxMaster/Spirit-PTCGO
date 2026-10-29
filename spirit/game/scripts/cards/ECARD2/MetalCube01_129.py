"""STUB: effect not implemented — do not guess mechanics.
Metal Cube 01 (ECARD2 #129): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Metal Pokémon in play. That Pokémon may use this card's attack instead of its own. At the end of your turn, discard Metal Cube 01.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="87584bc2-9241-51ed-b3b0-368b1887fa61",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MetalCube01.Name",
    display_name="Metal Cube 01",
    searchable_by=["Metal Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=129,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
