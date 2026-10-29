"""STUB: effect not implemented — do not guess mechanics.
Pokémon Fan Club (SM5 #133): trainer effect stubbed.

Card text:
  - Search your deck for up to 2 Basic Pokémon, reveal them, and put them into your hand. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="ff12d892-5b1d-5aca-a2a3-2a0039a4c3fc",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonFanClub.Name",
    display_name="Pokémon Fan Club",
    searchable_by=["Pok\u00e9mon Fan Club", "Supporter"],
    subtypes=["Supporter"],
    collector_number=133,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
