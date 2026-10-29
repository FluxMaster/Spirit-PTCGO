"""STUB: effect not implemented — do not guess mechanics.
Potion (BASE4 #122): trainer effect stubbed.

Card text:
  - Remove up to 2 damage counters from 1 of your Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c6ba229a-85b5-57fc-8a51-c88e316c61b8",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion"],
    subtypes=[],
    collector_number=122,
    set_code="BASE4",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
