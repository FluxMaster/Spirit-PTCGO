"""STUB: effect not implemented — do not guess mechanics.
Lake Boundary (DP2 #112): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Apply Weakness for each Pokémon (both yours and your opponent's) as ×2 instead.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="e58275a2-d98b-5056-acea-4a4170041551",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LakeBoundary.Name",
    display_name="Lake Boundary",
    searchable_by=["Lake Boundary", "Stadium"],
    subtypes=["Stadium"],
    collector_number=112,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
