"""STUB: effect not implemented — do not guess mechanics.
Potion (ECARD1 #156): trainer effect stubbed.

Card text:
  - Remove 2 damage counters from 1 of your Pokémon (1 if that Pokémon has only 1).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="7d1f2e4f-9288-50d2-8817-3521f9b40e2c",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion"],
    subtypes=[],
    collector_number=156,
    set_code="ECARD1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
