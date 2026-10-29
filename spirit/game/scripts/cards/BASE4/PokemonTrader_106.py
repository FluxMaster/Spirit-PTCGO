"""STUB: effect not implemented — do not guess mechanics.
Pokémon Trader (BASE4 #106): trainer effect stubbed.

Card text:
  - Trade 1 of the Basic Pokémon or Evolution cards in your hand for 1 of the Basic Pokémon or Evolution cards from your deck. Show both cards to your opponent. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="6a3860e7-3fd7-5044-8682-f5dd5d92d8c9",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonTrader.Name",
    display_name="Pokémon Trader",
    searchable_by=["Pok\u00e9mon Trader"],
    subtypes=[],
    collector_number=106,
    set_code="BASE4",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
