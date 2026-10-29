"""STUB: effect not implemented — do not guess mechanics.
Sabrina (GYM2 #20): trainer effect stubbed.

Card text:
  - Take all Energy cards attached to 1 of your Pokémon with Sabrina in its name and attach them to another 1 of your Pokémon with Sabrina in its name.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="69ea82da-eaef-5520-9381-7ee0353710e6",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Sabrina.Name",
    display_name="Sabrina",
    searchable_by=["Sabrina"],
    subtypes=[],
    collector_number=20,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
