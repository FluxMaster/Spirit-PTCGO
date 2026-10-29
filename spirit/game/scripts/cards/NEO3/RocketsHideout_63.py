"""STUB: effect not implemented — do not guess mechanics.
Rocket's Hideout (NEO3 #63): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Each Pokémon in play with Dark in its name (even your opponent's) gets +20 HP.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="285d5abd-00ed-50d6-903c-6bd5fd3f1cc1",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsHideout.Name",
    display_name="Rocket's Hideout",
    searchable_by=["Rocket's Hideout", "Stadium"],
    subtypes=["Stadium"],
    collector_number=63,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
