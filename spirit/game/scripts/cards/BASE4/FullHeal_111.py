"""STUB: effect not implemented — do not guess mechanics.
Full Heal (BASE4 #111): trainer effect stubbed.

Card text:
  - Your Active Pokémon is no longer Asleep, Confused, Paralyzed, or Poisoned.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ae12c97a-134a-5df1-8b38-bb69fec3580a",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullHeal.Name",
    display_name="Full Heal",
    searchable_by=["Full Heal"],
    subtypes=[],
    collector_number=111,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
