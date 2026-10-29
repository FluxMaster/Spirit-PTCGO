"""STUB: effect not implemented — do not guess mechanics.
Professor Oak (BASE4 #116): trainer effect stubbed.

Card text:
  - Discard your hand, then draw 7 cards.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="2843a9a2-e8a6-5563-bbdb-368206b29ae9",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOak.Name",
    display_name="Professor Oak",
    searchable_by=["Professor Oak"],
    subtypes=[],
    collector_number=116,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
