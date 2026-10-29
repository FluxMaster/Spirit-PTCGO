"""STUB: effect not implemented — do not guess mechanics.
Professor Oak (BASE1 #88): trainer effect stubbed.

Card text:
  - Discard your hand, then draw 7 cards.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ae3252b8-e1cc-5290-9385-a1d6b276ac79",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOak.Name",
    display_name="Professor Oak",
    searchable_by=["Professor Oak"],
    subtypes=[],
    collector_number=88,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
