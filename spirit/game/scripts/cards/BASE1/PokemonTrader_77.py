"""STUB: effect not implemented — do not guess mechanics.
Pokémon Trader (BASE1 #77): trainer effect stubbed.

Card text:
  - Trade 1 of the Basic Pokémon or Evolution cards in your hand for 1 of the Basic Pokémon or Evolution cards from your deck. Show both cards to your opponent. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b3553020-045b-563b-b097-f23232244309",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonTrader.Name",
    display_name="Pokémon Trader",
    searchable_by=["Pok\u00e9mon Trader"],
    subtypes=[],
    collector_number=77,
    set_code="BASE1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
