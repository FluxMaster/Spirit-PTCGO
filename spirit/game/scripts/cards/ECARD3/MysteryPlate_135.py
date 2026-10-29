"""STUB: effect not implemented — do not guess mechanics.
Mystery Plate γ (ECARD3 #135): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Pokémon in play. That Pokémon may use this card's attack instead of its own. At the end of your turn, discard Mystery Plate γ.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="2df7341b-3e56-5074-bb39-e25cf8758790",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteryPlate.Name",
    display_name="Mystery Plate γ",
    searchable_by=["Mystery Plate \u03b3", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=135,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
