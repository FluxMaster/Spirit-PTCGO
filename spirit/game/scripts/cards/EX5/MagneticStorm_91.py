"""STUB: effect not implemented — do not guess mechanics.
Magnetic Storm (EX5 #91): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Any damage done by attacks from Psychic Pokémon and Fighting Pokémon (both yours and your opponent's) is not affected by Resistance.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="559444fd-2fd8-5ce1-ad6a-0c3eaeb7cb01",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MagneticStorm.Name",
    display_name="Magnetic Storm",
    searchable_by=["Magnetic Storm", "Stadium"],
    subtypes=["Stadium"],
    collector_number=91,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
