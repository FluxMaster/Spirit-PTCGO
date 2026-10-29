"""STUB: effect not implemented — do not guess mechanics.
Super Rod (NEO1 #103): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, put an Evolution card from your discard pile, if any, into your hand. If tails, put a Basic Pokémon card from your discard pile, if any, into your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="5c8e39bb-40ac-5a2b-8dc4-8a6e77911cfd",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperRod.Name",
    display_name="Super Rod",
    searchable_by=["Super Rod"],
    subtypes=[],
    collector_number=103,
    set_code="NEO1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
