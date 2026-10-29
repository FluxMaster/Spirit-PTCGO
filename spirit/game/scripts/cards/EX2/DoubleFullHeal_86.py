"""STUB: effect not implemented — do not guess mechanics.
Double Full Heal (EX2 #86): trainer effect stubbed.

Card text:
  - Remove all Special Conditions from each of your Active Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="f3e6769c-7baa-58f8-b2a6-fe2be6793e39",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DoubleFullHeal.Name",
    display_name="Double Full Heal",
    searchable_by=["Double Full Heal", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="EX2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
