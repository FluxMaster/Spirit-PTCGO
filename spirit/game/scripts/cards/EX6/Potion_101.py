"""STUB: effect not implemented — do not guess mechanics.
Potion (EX6 #101): trainer effect stubbed.

Card text:
  - Remove 2 damage counters from 1 of your Pokémon (remove 1 damage counter if that Pokémon has only 1).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="61d986d2-732f-52c8-9036-f83216df1fde",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=101,
    set_code="EX6",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
