"""STUB: effect not implemented — do not guess mechanics.
Dragon Talon (DM #59): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - If the Dragon Pokémon this card is attached to is your Active Pokémon and is damaged by an opponent's attack (even if that Pokémon is Knocked Out), put 3 damage counters on the Attacking Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="992c7f18-3422-5fd5-9ae7-a6b78f90a5e2",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DragonTalon.Name",
    display_name="Dragon Talon",
    searchable_by=["Dragon Talon", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=59,
    set_code="DM",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
