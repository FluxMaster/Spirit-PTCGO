"""STUB: effect not implemented — do not guess mechanics.
Hustle Belt (SM7 #134): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - If the Pokémon this card is attached to has 30 HP or less remaining and has any damage counters on it, its attacks do 60 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="49e3b91b-b484-5d93-947b-c98ce10f2026",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HustleBelt.Name",
    display_name="Hustle Belt",
    searchable_by=["Hustle Belt", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=134,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
