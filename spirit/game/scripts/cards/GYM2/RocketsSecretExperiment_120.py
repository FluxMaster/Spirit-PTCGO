"""STUB: effect not implemented — do not guess mechanics.
Rocket's Secret Experiment (GYM2 #120): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, search your deck for any card and put it into your hand. Shuffle your deck afterward. If tails, you can't play Trainer cards until the end of your next turn.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="1ae6d970-ac31-55fd-b0e0-24e7cfbd7f74",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsSecretExperiment.Name",
    display_name="Rocket's Secret Experiment",
    searchable_by=["Rocket's Secret Experiment"],
    subtypes=[],
    collector_number=120,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
