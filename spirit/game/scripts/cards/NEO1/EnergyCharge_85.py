"""STUB: effect not implemented — do not guess mechanics.
Energy Charge (NEO1 #85): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, shuffle up to 2 Energy cards from your discard pile into your deck.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="1b0c3704-6d95-58ed-b892-a29de4a0ae54",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyCharge.Name",
    display_name="Energy Charge",
    searchable_by=["Energy Charge"],
    subtypes=[],
    collector_number=85,
    set_code="NEO1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
