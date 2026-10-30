"""STUB: effect not implemented — do not guess mechanics.
Desert Ruins (EX5 #88): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - At any time between turns, each player puts 1 damage counter on his or her Pokémon-ex with maximum HP of at least 100.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="e17f316c-a8b4-558f-ac0e-b86100d04a26",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DesertRuins.Name",
    display_name="Desert Ruins",
    searchable_by=["Desert Ruins", "Stadium"],
    subtypes=["Stadium"],
    collector_number=88,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
