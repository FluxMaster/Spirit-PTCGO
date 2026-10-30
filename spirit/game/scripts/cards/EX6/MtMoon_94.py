"""STUB: effect not implemented — do not guess mechanics.
Mt. Moon (EX6 #94): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Any Pokémon (both yours and your opponent's) with maximum HP less than 70 can't use any Poké-Powers.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="71fb1a9d-63cb-5cee-af3c-cc7c8202a493",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MtMoon.Name",
    display_name="Mt. Moon",
    searchable_by=["Mt. Moon", "Stadium"],
    subtypes=["Stadium"],
    collector_number=94,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
