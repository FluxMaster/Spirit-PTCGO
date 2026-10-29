"""STUB: effect not implemented — do not guess mechanics.
Plumeria (SM3 #145): trainer effect stubbed.

Card text:
  - Discard 2 cards from your hand. If you do, discard an Energy attached to 1 of your opponent's Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="16bc444e-26f7-5fbc-b21d-7655d5b2aba7",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Plumeria.Name",
    display_name="Plumeria",
    searchable_by=["Plumeria", "Supporter"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="SM3",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
