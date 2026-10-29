"""STUB: effect not implemented — do not guess mechanics.
Mystery Plate δ (ECARD3 #136): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Pokémon in play. That Pokémon may use this card's attack instead of its own. At the end of your turn, discard Mystery Plate δ.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="80309a3f-6cbc-5966-b3af-13753e616cdd",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteryPlate.Name",
    display_name="Mystery Plate δ",
    searchable_by=["Mystery Plate \u03b4", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=136,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
