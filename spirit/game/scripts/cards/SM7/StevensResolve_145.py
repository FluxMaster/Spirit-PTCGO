"""STUB: effect not implemented — do not guess mechanics.
Steven's Resolve (SM7 #145): trainer effect stubbed.

Card text:
  - Search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck. Your turn ends.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="e274e0be-74d8-58c2-b796-9200f85d3341",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StevensResolve.Name",
    display_name="Steven's Resolve",
    searchable_by=["Steven's Resolve", "Supporter"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="SM7",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
