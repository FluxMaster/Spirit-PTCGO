"""STUB: effect not implemented — do not guess mechanics.
Potion (TK1B #8): trainer effect stubbed.

Card text:
  - Remove 2 damage counters from 1 of your Pokémon (remove 1 damage counter if that Pokémon has only 1).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b99f85cc-2524-54ed-bcea-11dd3f7dd5cb",
    key="TK1B",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=8,
    set_code="TK1B",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
