"""STUB: effect not implemented — do not guess mechanics.
Maintenance (BASE1 #83): trainer effect stubbed.

Card text:
  - Shuffle 2 of the other cards from your hand into your deck in order to draw a card.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="637b0637-f28f-5e86-879f-a65742999194",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Maintenance.Name",
    display_name="Maintenance",
    searchable_by=["Maintenance"],
    subtypes=[],
    collector_number=83,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
