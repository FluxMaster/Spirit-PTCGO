"""STUB: effect not implemented — do not guess mechanics.
Misty's Wrath (GYM1 #114): trainer effect stubbed.

Card text:
  - Look at the top 7 cards of your deck. Choose 2 of those cards and put them into your hand. Discard the rest.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="98f60aaa-c7ea-5224-9da1-4051fba17a03",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysWrath.Name",
    display_name="Misty's Wrath",
    searchable_by=["Misty's Wrath"],
    subtypes=[],
    collector_number=114,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
