"""STUB: effect not implemented — do not guess mechanics.
Energy Charge (EX8 #86): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, search your discard pile for 2 Energy cards (1 if there is only 1), show them to your opponent, and shuffle them into your deck.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="f19d4531-d8d0-579d-a216-292a4d5510a9",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyCharge.Name",
    display_name="Energy Charge",
    searchable_by=["Energy Charge", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
