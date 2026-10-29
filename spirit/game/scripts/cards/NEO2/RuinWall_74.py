"""STUB: effect not implemented — do not guess mechanics.
Ruin Wall (NEO2 #74): trainer effect stubbed.

Card text:
  - Search your deck for a card with Unown in its name and put it onto your Bench. Shuffle your deck afterward. (You can't play this card if your Bench is full.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="a0881ca1-94ef-5432-a287-d0ba20123a69",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RuinWall.Name",
    display_name="Ruin Wall",
    searchable_by=["Ruin Wall"],
    subtypes=[],
    collector_number=74,
    set_code="NEO2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
