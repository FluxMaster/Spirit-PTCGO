"""STUB: effect not implemented — do not guess mechanics.
Ultra Forest Kartenvoy (SM10 #188): trainer effect stubbed.

Card text:
  - During this turn, damage from your Ultra Beasts' attacks isn't affected by any effects on your opponent's Active Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="fe8c8dc0-70d8-5b82-a12b-981517ad54e0",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UltraForestKartenvoy.Name",
    display_name="Ultra Forest Kartenvoy",
    searchable_by=["Ultra Forest Kartenvoy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=188,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
