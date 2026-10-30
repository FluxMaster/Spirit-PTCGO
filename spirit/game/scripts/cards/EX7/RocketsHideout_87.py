"""STUB: effect not implemented — do not guess mechanics.
Rocket's Hideout (EX7 #87): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Each Pokémon with Dark or Rocket's in its name (both yours and your opponent's) gets +20 HP.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="7b303c09-977b-5677-b49b-b046831085bf",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RocketsHideout.Name",
    display_name="Rocket's Hideout",
    searchable_by=["Rocket's Hideout", "Stadium"],
    subtypes=["Stadium"],
    collector_number=87,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
