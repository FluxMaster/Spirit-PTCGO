"""STUB: effect not implemented — do not guess mechanics.
Nita (SM9 #151): trainer effect stubbed.

Card text:
  - You can play this card only if your opponent's Active Pokémon is a Basic Pokémon.
  - Put an Energy from your opponent's Active Pokémon on top of their deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="03b884f8-71a8-568c-af53-370d48ae2ebb",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Nita.Name",
    display_name="Nita",
    searchable_by=["Nita", "Supporter"],
    subtypes=["Supporter"],
    collector_number=151,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
