"""STUB: effect not implemented — do not guess mechanics.
Double Full Heal (DP1 #105): trainer effect stubbed.

Card text:
  - Remove all Special Conditions from each of your Active Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b89520b6-d5b9-57bb-8185-9ed7e283fdb1",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DoubleFullHeal.Name",
    display_name="Double Full Heal",
    searchable_by=["Double Full Heal", "Item"],
    subtypes=["Item"],
    collector_number=105,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
