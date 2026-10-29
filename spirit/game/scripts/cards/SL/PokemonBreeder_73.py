"""STUB: effect not implemented — do not guess mechanics.
Pokémon Breeder (SL #73): trainer effect stubbed.

Card text:
  - Draw 2 cards and heal 20 damage from your Active Pokémon. If you have no cards in your deck, you can't play this card.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="e3d53a72-4e15-5199-a727-57e92c8346ba",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonBreeder.Name",
    display_name="Pokémon Breeder",
    searchable_by=["Pok\u00e9mon Breeder", "Supporter"],
    subtypes=["Supporter"],
    collector_number=73,
    set_code="SL",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
