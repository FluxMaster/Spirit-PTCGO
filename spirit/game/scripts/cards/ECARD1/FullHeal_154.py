"""STUB: effect not implemented — do not guess mechanics.
Full Heal (ECARD1 #154): trainer effect stubbed.

Card text:
  - Remove all Special Conditions from your Active Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e150f477-7bda-5a72-9e4a-0907f01e7e9c",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullHeal.Name",
    display_name="Full Heal",
    searchable_by=["Full Heal"],
    subtypes=[],
    collector_number=154,
    set_code="ECARD1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
