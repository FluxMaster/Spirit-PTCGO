"""STUB: effect not implemented — do not guess mechanics.
Low Pressure System (EX3 #86): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play.
  - Each Grass and Lightning Pokémon in play (both yours and your opponent's) gets +10 HP.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="f6ed8a60-ba95-5aeb-bac2-ee619b612f81",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LowPressureSystem.Name",
    display_name="Low Pressure System",
    searchable_by=["Low Pressure System", "Stadium"],
    subtypes=["Stadium"],
    collector_number=86,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
