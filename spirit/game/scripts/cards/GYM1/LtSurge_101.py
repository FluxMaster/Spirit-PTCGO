"""STUB: effect not implemented — do not guess mechanics.
Lt. Surge (GYM1 #101): trainer effect stubbed.

Card text:
  - You can play this card only if you have at least 1 Basic Pokémon card in your hand. Put a Basic Pokémon card from your hand into play as your Active Pokémon. Put your old Active Pokémon onto your Bench. (You can't play this card if your Bench is full.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="4af0f412-55ba-53d3-a3a5-ef0f37835c01",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LtSurge.Name",
    display_name="Lt. Surge",
    searchable_by=["Lt. Surge"],
    subtypes=[],
    collector_number=101,
    set_code="GYM1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
