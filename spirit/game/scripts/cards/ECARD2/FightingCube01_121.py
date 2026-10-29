"""STUB: effect not implemented — do not guess mechanics.
Fighting Cube 01 (ECARD2 #121): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Fighting Pokémon in play. That Pokémon my use this card's attack instead of its own. At the end of your turn, discard Fighting Cube 01.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="8f288a6d-2d07-553c-9a8c-63c0cfabd9a4",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FightingCube01.Name",
    display_name="Fighting Cube 01",
    searchable_by=["Fighting Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=121,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
