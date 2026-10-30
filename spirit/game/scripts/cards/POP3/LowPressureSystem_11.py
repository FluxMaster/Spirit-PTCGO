"""STUB: effect not implemented — do not guess mechanics.
Low Pressure System (POP3 #11): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Each Grass and Lightning Pokémon in play (both yours and your opponent's) gets +10 HP.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="7ad2a543-f166-5159-8471-289c581f147a",
    key="POP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LowPressureSystem.Name",
    display_name="Low Pressure System",
    searchable_by=["Low Pressure System", "Stadium"],
    subtypes=["Stadium"],
    collector_number=11,
    set_code="POP3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
