"""STUB: effect not implemented — do not guess mechanics.
Miracle Sphere γ (ECARD3 #131): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Evolved Grass, Water, or Lightning Pokémon in play. That Pokémon may use this card's attack instead of its own. At the end of your turn, discard Miracle Sphere γ.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="3ffafd21-663f-59fb-b757-499119bed57a",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MiracleSphere.Name",
    display_name="Miracle Sphere γ",
    searchable_by=["Miracle Sphere \u03b3", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=131,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
