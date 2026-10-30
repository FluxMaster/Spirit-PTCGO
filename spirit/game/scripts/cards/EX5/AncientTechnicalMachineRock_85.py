"""STUB: effect not implemented — do not guess mechanics.
Ancient Technical Machine [Rock] (EX5 #85): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Evolved Pokémon (excluding Pokémon-ex and Pokémon that has an owner in its name) in play. That Pokémon may use this card's attack instead of its own. At the end of your turn, discard Ancient Technical Machine [Rock].
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="46dd72ab-5db3-532a-9c67-153cb44cdbc1",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientTechnicalMachineRock.Name",
    display_name="Ancient Technical Machine [Rock]",
    searchable_by=["Ancient Technical Machine [Rock]", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=85,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
