"""STUB: effect not implemented — do not guess mechanics.
Sprout Tower (NEO1 #97): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - All damage done by Colorless Pokémon's attacks is reduced by 30 (after applying Weakness and Resistance).
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="f23f97e2-ad14-5c48-82f6-a579786983fa",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SproutTower.Name",
    display_name="Sprout Tower",
    searchable_by=["Sprout Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=97,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
