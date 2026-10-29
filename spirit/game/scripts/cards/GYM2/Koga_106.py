"""STUB: effect not implemented — do not guess mechanics.
Koga (GYM2 #106): trainer effect stubbed.

Card text:
  - If an attack from a Pokémon with Koga in its name does damage to a Defending Pokémon this turn, that Pokémon is then Poisoned.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="cc32b87f-4cca-5a0c-bf60-b5e3fd4f1cf3",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Koga.Name",
    display_name="Koga",
    searchable_by=["Koga"],
    subtypes=[],
    collector_number=106,
    set_code="GYM2",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
