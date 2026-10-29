"""STUB: effect not implemented — do not guess mechanics.
Lt. Surge (GYM1 #17): trainer effect stubbed.

Card text:
  - You can play this card only if you have at least 1 Basic Pokémon card in your hand. Put a Basic Pokémon card from your hand into play as your Active Pokémon. Put your old Active Pokémon onto your Bench. (You can't play this card if your Bench is full.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="fdfe2f97-6c95-5e31-a180-1d6b21f7f82a",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LtSurge.Name",
    display_name="Lt. Surge",
    searchable_by=["Lt. Surge"],
    subtypes=[],
    collector_number=17,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
