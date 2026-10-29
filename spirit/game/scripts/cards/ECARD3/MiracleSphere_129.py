"""STUB: effect not implemented — do not guess mechanics.
Miracle Sphere α (ECARD3 #129): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Evolved Fire, Lightning, or Fighting Pokémon in play. That Pokémon may use this card's attack instead of its own. At the end of your turn, discard Miracle Plate α.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="a3d4bb05-9af5-5fd7-b5e4-c5266ebf9123",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MiracleSphere.Name",
    display_name="Miracle Sphere α",
    searchable_by=["Miracle Sphere \u03b1", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=129,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
