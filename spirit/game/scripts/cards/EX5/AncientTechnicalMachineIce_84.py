"""STUB: effect not implemented — do not guess mechanics.
Ancient Technical Machine [Ice] (EX5 #84): trainer effect stubbed.

Card text:
  - Attach this card to 1 of your Evolved Pokémon (excluding Pokémon-ex and Pokémon that has an owner in its name) in play. That Pokémon may use this card's attack instead of its own. At the end of your turn, discard Ancient Technical Machine [Ice].
"""

from spirit.game.data_utils import TrainerCardDef, unimplemented
from spirit.game.attributes import Rarities, TrainerType

card = TrainerCardDef(
    guid="c13abb70-a9c8-5f6f-a79d-f6d4538ee2dd",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientTechnicalMachineIce.Name",
    display_name="Ancient Technical Machine [Ice]",
    searchable_by=["Ancient Technical Machine [Ice]", "Technical Machine"],
    subtypes=["Technical Machine"],
    collector_number=84,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    trainer_type=TrainerType.TECHNICAL_MACHINE,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
