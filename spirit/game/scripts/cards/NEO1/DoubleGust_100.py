"""STUB: effect not implemented — do not guess mechanics.
Double Gust (NEO1 #100): trainer effect stubbed.

Card text:
  - If you have any Benched Pokémon, your opponent chooses 1 of them and switches it with your Active Pokémon. Then, if your opponent has any Benched Pokémon, choose 1 of them and switch it with his or her Active Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="573a33f6-0b84-52c8-8685-e57e533c76f6",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DoubleGust.Name",
    display_name="Double Gust",
    searchable_by=["Double Gust"],
    subtypes=[],
    collector_number=100,
    set_code="NEO1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
