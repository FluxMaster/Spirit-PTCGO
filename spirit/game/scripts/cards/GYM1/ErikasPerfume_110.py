"""STUB: effect not implemented — do not guess mechanics.
Erika's Perfume (GYM1 #110): trainer effect stubbed.

Card text:
  - Look at your opponent's hand. If he or she has any Basic Pokémon cards there, you may put any number of them onto your opponent's Bench (as long as there's room).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c4c84d52-9fdd-59ae-bfc5-f6d4dce6972e",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ErikasPerfume.Name",
    display_name="Erika's Perfume",
    searchable_by=["Erika's Perfume"],
    subtypes=[],
    collector_number=110,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
