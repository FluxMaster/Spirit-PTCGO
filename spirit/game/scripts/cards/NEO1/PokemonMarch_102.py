"""STUB: effect not implemented — do not guess mechanics.
Pokémon March (NEO1 #102): trainer effect stubbed.

Card text:
  - Your opponent may search his or her deck for 1 Basic Pokémon card and put it onto his or her Bench. Then, you may search your deck for 1 Basic Pokémon card and put it onto your Bench. Then, each player shuffles his or her deck. (A player can't do any of this if his or her Bench is full.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="fa51c915-8eac-504b-86a9-c5f695a61cbe",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonMarch.Name",
    display_name="Pokémon March",
    searchable_by=["Pok\u00e9mon March"],
    subtypes=[],
    collector_number=102,
    set_code="NEO1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
