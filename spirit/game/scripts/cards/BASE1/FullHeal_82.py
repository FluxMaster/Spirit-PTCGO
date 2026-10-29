"""STUB: effect not implemented — do not guess mechanics.
Full Heal (BASE1 #82): trainer effect stubbed.

Card text:
  - Your Active Pokémon is no longer Asleep, Confused, Paralyzed, or Poisoned.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="8990de97-d63d-58f7-9c11-5d3b4cd030fd",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FullHeal.Name",
    display_name="Full Heal",
    searchable_by=["Full Heal"],
    subtypes=[],
    collector_number=82,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
