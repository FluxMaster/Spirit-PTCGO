"""STUB: effect not implemented — do not guess mechanics.
Metal Core Barrier (SM10 #232): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - If this card is attached to 1 of your Pokémon, discard it at the end of your opponent's turn.
  - The Metal Pokémon this card is attached to takes 70 less damage from your opponent's attacks (after applying Weakness and Resistance).
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="cef2d1c4-371e-5489-b6dd-f1246929f4a2",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MetalCoreBarrier.Name",
    display_name="Metal Core Barrier",
    searchable_by=["Metal Core Barrier", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=232,
    set_code="SM10",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
