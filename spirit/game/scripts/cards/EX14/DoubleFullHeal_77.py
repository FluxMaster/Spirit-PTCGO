"""STUB: effect not implemented — do not guess mechanics.
Double Full Heal (EX14 #77): trainer effect stubbed.

Card text:
  - Remove all Special Conditions from each of your Active Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="70e20f9b-7494-5ab1-bf30-4b3619ffcac9",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DoubleFullHeal.Name",
    display_name="Double Full Heal",
    searchable_by=["Double Full Heal", "Item"],
    subtypes=["Item"],
    collector_number=77,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
