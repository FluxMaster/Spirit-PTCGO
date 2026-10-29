"""STUB: effect not implemented — do not guess mechanics.
Plumeria (SM3 #120): trainer effect stubbed.

Card text:
  - Discard 2 cards from your hand. If you do, discard an Energy from 1 of your opponent's Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="081907e9-09b4-59a9-be15-a5d82e91d927",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Plumeria.Name",
    display_name="Plumeria",
    searchable_by=["Plumeria", "Supporter"],
    subtypes=["Supporter"],
    collector_number=120,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
