"""STUB: effect not implemented — do not guess mechanics.
Nita (SM9 #180): trainer effect stubbed.

Card text:
  - You can play this card only if your opponent's Active Pokémon is a Basic Pokémon.
  - Put an Energy from your opponent's Active Pokémon on top of their deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="57d76f7d-3945-5fa2-9f05-70c2b717c650",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Nita.Name",
    display_name="Nita",
    searchable_by=["Nita", "Supporter"],
    subtypes=["Supporter"],
    collector_number=180,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
