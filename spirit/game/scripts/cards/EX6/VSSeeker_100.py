"""STUB: effect not implemented — do not guess mechanics.
VS Seeker (EX6 #100): trainer effect stubbed.

Card text:
  - Search your discard pile for a Supporter card, show it to your opponent, and put it into your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="0daf3ae6-be85-5a7e-9d62-44327f84e1ed",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VSSeeker.Name",
    display_name="VS Seeker",
    searchable_by=["VS Seeker", "Item"],
    subtypes=["Item"],
    collector_number=100,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
