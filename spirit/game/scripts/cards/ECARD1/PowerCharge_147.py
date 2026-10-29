"""STUB: effect not implemented — do not guess mechanics.
Power Charge (ECARD1 #147): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, shuffle 2 Energy cards from your discard pile into your deck (1 if you have only 1).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="56208084-623c-554a-821e-d1c9334e0ac6",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PowerCharge.Name",
    display_name="Power Charge",
    searchable_by=["Power Charge"],
    subtypes=[],
    collector_number=147,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
