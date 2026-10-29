"""STUB: effect not implemented — do not guess mechanics.
Mystery Plate α (ECARD3 #133): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Pokémon in play. That Pokémon may use this card's attack instead of its own. At the end of your turn, discard Mystery Plate α.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="515fe3e5-53e1-55f4-a1f8-bd47e4158edd",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteryPlate.Name",
    display_name="Mystery Plate α",
    searchable_by=["Mystery Plate \u03b1", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=133,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
