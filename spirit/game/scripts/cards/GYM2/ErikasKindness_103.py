"""STUB: effect not implemented — do not guess mechanics.
Erika's Kindness (GYM2 #103): trainer effect stubbed.

Card text:
  - Remove 2 damage counters from each Pokémon (yours and your opponent's) with any damage counters on it. If a Pokémon has just 1 damage counter, remove it.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="230115f3-ff70-5fa7-8020-3b524848fb72",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ErikasKindness.Name",
    display_name="Erika's Kindness",
    searchable_by=["Erika's Kindness"],
    subtypes=[],
    collector_number=103,
    set_code="GYM2",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
