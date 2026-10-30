"""STUB: effect not implemented — do not guess mechanics.
Pokémon Retriever (EX7 #84): trainer effect stubbed.

Card text:
  - Search your discard pile for Basic Pokémon and Evolution cards. You may either show 1 Basic Pokémon or Evolution card to your opponent and put it into your hand, or show a combination of 3 Basic Pokémon or Evolution cards to your opponent and shuffle them into your deck.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c2824a97-1f80-5265-9046-a88d3763f435",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonRetriever.Name",
    display_name="Pokémon Retriever",
    searchable_by=["Pok\u00e9mon Retriever", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=84,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
