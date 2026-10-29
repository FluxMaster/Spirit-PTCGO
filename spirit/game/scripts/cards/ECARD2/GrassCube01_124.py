"""STUB: effect not implemented — do not guess mechanics.
Grass Cube 01 (ECARD2 #124): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Grass Pokémon in play. That Pokémon may use this card's attack instead of its own. At the end of your turn, discard Grass Cube 01.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="a7ab2f81-e315-5718-8609-c1b3d67d6e68",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GrassCube01.Name",
    display_name="Grass Cube 01",
    searchable_by=["Grass Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=124,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
