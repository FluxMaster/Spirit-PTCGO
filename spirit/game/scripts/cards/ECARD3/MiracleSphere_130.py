"""STUB: effect not implemented — do not guess mechanics.
Miracle Sphere β (ECARD3 #130): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Evolved Fire, Water, or Psychic Pokémon in play. That Pokémon may use this card's attack instead of its own. At the end of your turn, discard Miracle Sphere β.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="b3449b56-08c4-5ed5-b680-0d0609437ac7",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MiracleSphere.Name",
    display_name="Miracle Sphere β",
    searchable_by=["Miracle Sphere \u03b2", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=130,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
