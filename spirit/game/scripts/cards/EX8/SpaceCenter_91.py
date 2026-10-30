"""STUB: effect not implemented — do not guess mechanics.
Space Center (EX8 #91): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Ignore Poké-Bodies for all Basic Pokémon in play (both yours and your opponent's) (excluding Pokémon-ex and Pokémon that has an owner in its name).
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="f4f6c5fa-54c9-547d-a81e-dad8f2747207",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpaceCenter.Name",
    display_name="Space Center",
    searchable_by=["Space Center", "Stadium"],
    subtypes=["Stadium"],
    collector_number=91,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
