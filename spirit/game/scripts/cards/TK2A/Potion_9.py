"""STUB: effect not implemented — do not guess mechanics.
Potion (TK2A #9): trainer effect stubbed.

Card text:
  - Remove 2 damage counters from 1 of your Pokémon (remove 1 damage counter if that Pokémon has only 1).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="993fbf30-40ee-53fa-a381-c334a557c450",
    key="TK2A",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=9,
    set_code="TK2A",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
