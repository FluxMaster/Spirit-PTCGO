"""STUB: effect not implemented — do not guess mechanics.
Mystery Plate β (ECARD3 #134): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Pokémon in play. That Pokémon may use this card's attack instead of its own. At the end of your turn, discard Mystery Plate β.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="476b9808-6971-5be2-ad19-73e228ec2598",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteryPlate.Name",
    display_name="Mystery Plate β",
    searchable_by=["Mystery Plate \u03b2", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=134,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
