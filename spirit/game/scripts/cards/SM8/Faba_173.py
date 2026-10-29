"""STUB: effect not implemented — do not guess mechanics.
Faba (SM8 #173): trainer effect stubbed.

Card text:
  - Choose a Pokémon Tool or Special Energy card attached to 1 of your opponent's Pokémon, or any Stadium card in play, and put it in the Lost Zone.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="19b3fbda-0050-5089-b588-306b9114aec0",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Faba.Name",
    display_name="Faba",
    searchable_by=["Faba", "Supporter"],
    subtypes=["Supporter"],
    collector_number=173,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
