"""STUB: effect not implemented — do not guess mechanics.
High Pressure System (POP3 #10): trainer effect stubbed.

Card text:
  - This card stays in play when you play it. Discard this card if another Stadium card comes into play. If another card with the same name is in play, you can't play this card.
  - Each player pays Colorless less to retreat his or her Fire and Water Pokémon.
"""

from spirit.game.data_utils import StadiumCardDef, unimplemented
from spirit.game.attributes import Rarities

card = StadiumCardDef(
    guid="22d23a20-bb72-53d7-8e09-a339d007e94c",
    key="POP3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HighPressureSystem.Name",
    display_name="High Pressure System",
    searchable_by=["High Pressure System", "Stadium"],
    subtypes=["Stadium"],
    collector_number=10,
    set_code="POP3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
