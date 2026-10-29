"""STUB: effect not implemented — do not guess mechanics.
Darkness Cube 01 (ECARD2 #119): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Darkness Pokémon in play. That Pokémon may use this card's attack instead of its own. At the end of your turn, discard Darkness Cube 01.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="ebdc4f65-897f-548f-9d54-8deab3d4aabc",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DarknessCube01.Name",
    display_name="Darkness Cube 01",
    searchable_by=["Darkness Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=119,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
