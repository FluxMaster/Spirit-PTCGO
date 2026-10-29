"""STUB: effect not implemented — do not guess mechanics.
Flyinium Z: Air Slash (SM11 #195): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - If the Pokémon this card is attached to has the Air Slash attack, it can use the GX attack on this card. (You still need the necessary Energy to use this attack.)
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="72c96a35-d391-5e6f-9a4f-0cf9670a8c41",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FlyiniumZAirSlash.Name",
    display_name="Flyinium Z: Air Slash",
    searchable_by=["Flyinium Z: Air Slash", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=195,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
