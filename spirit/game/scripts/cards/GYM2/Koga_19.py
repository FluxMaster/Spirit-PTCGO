"""STUB: effect not implemented — do not guess mechanics.
Koga (GYM2 #19): trainer effect stubbed.

Card text:
  - If an attack from a Pokémon with Koga in its name does damage to a Defending Pokémon this turn, that Pokémon is then Poisoned.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="57d8742f-c836-583f-8d37-3fea4e074b1b",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Koga.Name",
    display_name="Koga",
    searchable_by=["Koga"],
    subtypes=[],
    collector_number=19,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
