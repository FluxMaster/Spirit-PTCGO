"""STUB: effect not implemented — do not guess mechanics.
Grimsley (SM11 #234): trainer effect stubbed.

Card text:
  - Move up to 3 damage counters from 1 of your opponent's Pokémon to another of their Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="ce0ad422-0c2b-5809-b9ef-7dcbaa198c04",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Grimsley.Name",
    display_name="Grimsley",
    searchable_by=["Grimsley", "Supporter"],
    subtypes=["Supporter"],
    collector_number=234,
    set_code="SM11",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
