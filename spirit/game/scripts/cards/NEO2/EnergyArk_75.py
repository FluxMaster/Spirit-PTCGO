"""STUB: effect not implemented — do not guess mechanics.
Energy Ark (NEO2 #75): trainer effect stubbed.

Card text:
  - Flip 2 coins. For each heads, search your deck for a Basic Energy card. Show that card to your opponent, then put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="67633335-3ee9-55b9-a277-d19f7bee9c65",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyArk.Name",
    display_name="Energy Ark",
    searchable_by=["Energy Ark"],
    subtypes=[],
    collector_number=75,
    set_code="NEO2",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
