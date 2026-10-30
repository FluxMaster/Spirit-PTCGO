"""STUB: effect not implemented — do not guess mechanics.
Ancient Technical Machine [Steel] (EX5 #86): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Evolved Pokémon (excluding Pokémon-ex and Pokémon that has an owner in its name) in play. That Pokémon may use this card's attack instead of its own. At the end of your turn, discard Ancient Technical Machine [Steel].
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="b3a71da2-8057-5887-94bc-ada52dbb6aec",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientTechnicalMachineSteel.Name",
    display_name="Ancient Technical Machine [Steel]",
    searchable_by=["Ancient Technical Machine [Steel]", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=86,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
