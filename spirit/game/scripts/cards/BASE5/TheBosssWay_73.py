"""STUB: effect not implemented — do not guess mechanics.
The Boss's Way (BASE5 #73): trainer effect stubbed.

Card text:
  - Search your deck for an Evolution card with Dark in its name. Show it to your opponent and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="6025b89d-bb5e-58d0-8a0a-4db9c5a6a2ea",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TheBosssWay.Name",
    display_name="The Boss's Way",
    searchable_by=["The Boss's Way"],
    subtypes=[],
    collector_number=73,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
