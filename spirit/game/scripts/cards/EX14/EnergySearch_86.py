"""STUB: effect not implemented — do not guess mechanics.
Energy Search (EX14 #86): trainer effect stubbed.

Card text:
  - Search your deck for a basic Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="69df534d-067c-5710-80b1-4517bc0ad4ea",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergySearch.Name",
    display_name="Energy Search",
    searchable_by=["Energy Search", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="EX14",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
