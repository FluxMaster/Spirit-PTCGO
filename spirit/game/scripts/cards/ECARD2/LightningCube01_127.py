"""STUB: effect not implemented — do not guess mechanics.
Lightning Cube 01 (ECARD2 #127): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Lightning Pokémon in play. That Pokémon may use this card's attack instead of its own. At the end of your turn, discard Lightning Cube 01.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="54711d47-a6a0-568e-9d1c-611671551d1c",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LightningCube01.Name",
    display_name="Lightning Cube 01",
    searchable_by=["Lightning Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=127,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
