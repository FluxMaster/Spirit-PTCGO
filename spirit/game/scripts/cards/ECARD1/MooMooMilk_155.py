"""STUB: effect not implemented — do not guess mechanics.
Moo-Moo Milk (ECARD1 #155): trainer effect stubbed.

Card text:
  - Choose 1 of your Pokémon. Flip 2 coins. Remove 2 damage counters times the number of heads from that Pokémon. If the Pokémon has fewer damage counters than that, remove all of them.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="6a320f3f-f2e9-5e37-8a41-2ef643856749",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MooMooMilk.Name",
    display_name="Moo-Moo Milk",
    searchable_by=["Moo-Moo Milk"],
    subtypes=[],
    collector_number=155,
    set_code="ECARD1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
