"""STUB: effect not implemented — do not guess mechanics.
Potion (EX14 #87): trainer effect stubbed.

Card text:
  - Remove 2 damage counters from 1 of your Pokémon (remove 1 damage counter if that Pokémon has only 1).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="dc77866f-0d84-527f-af8b-a2e88b40b10f",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=87,
    set_code="EX14",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
