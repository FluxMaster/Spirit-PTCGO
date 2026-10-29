"""STUB: effect not implemented — do not guess mechanics.
Goop Gas Attack (BASE5 #78): trainer effect stubbed.

Card text:
  - All Pokémon Powers stop working until the end of your opponent's next turn.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="426a5188-2c95-5fe9-b899-3393674d10f8",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GoopGasAttack.Name",
    display_name="Goop Gas Attack",
    searchable_by=["Goop Gas Attack"],
    subtypes=[],
    collector_number=78,
    set_code="BASE5",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
