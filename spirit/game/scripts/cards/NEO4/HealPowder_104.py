"""STUB: effect not implemented — do not guess mechanics.
Heal Powder (NEO4 #104): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, your Active Pokémon is no longer Asleep, Confused, Paralyzed, or Poisoned and remove 2 damage counters from it. If your Active Pokémon has fewer damage counters than that, remove all of them.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="644d3e22-e44d-58b6-b4ea-715016f5fe23",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HealPowder.Name",
    display_name="Heal Powder",
    searchable_by=["Heal Powder"],
    subtypes=[],
    collector_number=104,
    set_code="NEO4",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
