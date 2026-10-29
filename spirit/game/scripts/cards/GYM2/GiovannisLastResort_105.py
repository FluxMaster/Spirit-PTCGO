"""STUB: effect not implemented — do not guess mechanics.
Giovanni's Last Resort (GYM2 #105): trainer effect stubbed.

Card text:
  - Remove all damage counters from 1 of your Pokémon with Giovanni in its name. Then discard your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b909f055-1be4-5d3c-9e67-d58121a16176",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GiovannisLastResort.Name",
    display_name="Giovanni's Last Resort",
    searchable_by=["Giovanni's Last Resort"],
    subtypes=[],
    collector_number=105,
    set_code="GYM2",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
