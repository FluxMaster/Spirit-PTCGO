"""STUB: effect not implemented — do not guess mechanics.
Psychic Cube 01 (ECARD2 #132): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Psychic Pokémon in play. That Pokémon may us this card's attack instead of its own. At the end of your turn, discard Psychic Cube 01.
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="864afb6b-aea4-595d-8320-b04e5990d7a5",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PsychicCube01.Name",
    display_name="Psychic Cube 01",
    searchable_by=["Psychic Cube 01", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=132,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
