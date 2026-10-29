"""STUB: effect not implemented — do not guess mechanics.
Moo-Moo Milk (NEO1 #101): trainer effect stubbed.

Card text:
  - Choose 1 of your Pokémon. Flip 2 coins. Remove 2 damage counters times the number of heads from that Pokémon. If the Pokémon has fewer damage counters than that, remove all of them.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c8e3c6c2-8e83-583f-b734-d1f8d5c117da",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MooMooMilk.Name",
    display_name="Moo-Moo Milk",
    searchable_by=["Moo-Moo Milk"],
    subtypes=[],
    collector_number=101,
    set_code="NEO1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
