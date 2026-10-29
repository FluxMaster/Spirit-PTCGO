"""STUB: effect not implemented — do not guess mechanics.
Max Revive (GYM2 #117): trainer effect stubbed.

Card text:
  - Discard 2 Energy cards from your hand in order to put 1 Basic Pokémon from your discard pile onto your Bench. (You can't play Max Revive if your Bench is full.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="6c06b163-7499-5f94-a0ca-80499d4f493b",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxRevive.Name",
    display_name="Max Revive",
    searchable_by=["Max Revive"],
    subtypes=[],
    collector_number=117,
    set_code="GYM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
