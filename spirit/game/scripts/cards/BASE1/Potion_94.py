"""STUB: effect not implemented — do not guess mechanics.
Potion (BASE1 #94): trainer effect stubbed.

Card text:
  - Remove up to 2 damage counters from 1 of your Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d54dd009-991e-554a-a43e-cbc6b410056e",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion"],
    subtypes=[],
    collector_number=94,
    set_code="BASE1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
