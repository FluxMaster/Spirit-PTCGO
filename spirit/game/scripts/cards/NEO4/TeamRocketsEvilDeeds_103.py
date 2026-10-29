"""STUB: effect not implemented — do not guess mechanics.
Team Rocket's Evil Deeds (NEO4 #103): trainer effect stubbed.

Card text:
  - Look at your opponent's hand and choose a card there. Your opponent shuffles that card into his or her deck. Then, your opponent may draw up to 2 cards.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ff17bf31-7963-5204-9aeb-caae73a94664",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamRocketsEvilDeeds.Name",
    display_name="Team Rocket's Evil Deeds",
    searchable_by=["Team Rocket's Evil Deeds"],
    subtypes=[],
    collector_number=103,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
