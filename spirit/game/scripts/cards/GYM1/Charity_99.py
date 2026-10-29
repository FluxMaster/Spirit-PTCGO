"""STUB: effect not implemented — do not guess mechanics.
Charity (GYM1 #99): trainer effect stubbed.

Card text:
  - Attach Charity to your Active Pokémon. Unless that Pokémon gets Knocked Out, return Charity to your hand at the end of your turn. If that Pokémon attacks and does damage to the Defending Pokémon, you may reduce that damage by any amount (rounded to the nearest 10).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b0898764-db83-5141-afef-f86d276185f7",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Charity.Name",
    display_name="Charity",
    searchable_by=["Charity"],
    subtypes=[],
    collector_number=99,
    set_code="GYM1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
