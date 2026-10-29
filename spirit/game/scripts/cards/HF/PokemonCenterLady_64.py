"""STUB: effect not implemented — do not guess mechanics.
Pokémon Center Lady (HF #64): trainer effect stubbed.

Card text:
  - Heal 60 damage and remove all Special Conditions from 1 of your Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="c814e210-ce04-5c6d-9099-12f80c5a0112",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonCenterLady.Name",
    display_name="Pokémon Center Lady",
    searchable_by=["Pok\u00e9mon Center Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=64,
    set_code="HF",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
