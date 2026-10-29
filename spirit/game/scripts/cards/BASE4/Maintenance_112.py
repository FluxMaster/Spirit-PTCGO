"""STUB: effect not implemented — do not guess mechanics.
Maintenance (BASE4 #112): trainer effect stubbed.

Card text:
  - Shuffle 2 of the other cards from your hand into your deck in order to draw a card.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="66adede1-9e5d-5255-9003-2fd6298d0c60",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Maintenance.Name",
    display_name="Maintenance",
    searchable_by=["Maintenance"],
    subtypes=[],
    collector_number=112,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
