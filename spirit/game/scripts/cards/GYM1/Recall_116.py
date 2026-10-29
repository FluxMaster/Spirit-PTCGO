"""STUB: effect not implemented — do not guess mechanics.
Recall (GYM1 #116): trainer effect stubbed.

Card text:
  - For your attack this turn, your Active Pokémon can use any attack from its Basic Pokémon card or any Evolution card attached to it. (You still have to pay for that attack's Energy cost.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="21b819d6-ad55-5873-a6e9-e9ffcc3a01b0",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Recall.Name",
    display_name="Recall",
    searchable_by=["Recall"],
    subtypes=[],
    collector_number=116,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
