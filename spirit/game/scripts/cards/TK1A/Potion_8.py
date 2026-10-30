"""STUB: effect not implemented — do not guess mechanics.
Potion (TK1A #8): trainer effect stubbed.

Card text:
  - Remove 2 damage counters from 1 of your Pokémon (remove 1 damage counter if that Pokémon has only 1).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="11bd62dd-de9c-54a4-8e20-ffb34b023e13",
    key="TK1A",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=8,
    set_code="TK1A",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
