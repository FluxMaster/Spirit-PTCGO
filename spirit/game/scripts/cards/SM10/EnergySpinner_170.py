"""STUB: effect not implemented — do not guess mechanics.
Energy Spinner (SM10 #170): trainer effect stubbed.

Card text:
  - Search your deck for a basic Energy card, reveal it, and put it into your hand. If you go second and it's your first turn, search for up to 3 basic Energy cards instead of 1. Then, shuffle your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="db1ba32a-1034-5a63-b73d-1597c45a988e",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySpinner.Name",
    display_name="Energy Spinner",
    searchable_by=["Energy Spinner", "Item"],
    subtypes=["Item"],
    collector_number=170,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
