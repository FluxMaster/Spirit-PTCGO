"""STUB: effect not implemented — do not guess mechanics.
Beastite (SM12 #185): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The attacks of the Ultra Beast this card is attached to do 10 more damage to your opponent's Active Pokémon for each Prize card you have taken (before applying Weakness and Resistance).
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="b3138bdc-662a-53b3-b63f-dbf4ab9d0414",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Beastite.Name",
    display_name="Beastite",
    searchable_by=["Beastite", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=185,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
