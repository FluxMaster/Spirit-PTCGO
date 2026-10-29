"""STUB: effect not implemented — do not guess mechanics.
Pokémon Breeder (SL #63): trainer effect stubbed.

Card text:
  - Draw 2 cards and heal 20 damage from your Active Pokémon. If you have no cards in your deck, you can't play this card.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="4ab16c4a-4239-5ad8-8502-ea6bd5f0215f",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonBreeder.Name",
    display_name="Pokémon Breeder",
    searchable_by=["Pok\u00e9mon Breeder", "Supporter"],
    subtypes=["Supporter"],
    collector_number=63,
    set_code="SL",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
