"""STUB: effect not implemented — do not guess mechanics.
Karate Belt (SM11 #252): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - If you have more Prize cards remaining than your opponent, the attacks of the Pokémon this card is attached to cost Fighting less.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="a448d0e7-3b82-561a-be94-a375a343e4dc",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.KarateBelt.Name",
    display_name="Karate Belt",
    searchable_by=["Karate Belt", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=252,
    set_code="SM11",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
