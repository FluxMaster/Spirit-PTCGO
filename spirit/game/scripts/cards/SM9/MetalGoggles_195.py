"""STUB: effect not implemented — do not guess mechanics.
Metal Goggles (SM9 #195): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The Metal Pokémon this card is attached to takes 30 less damage from your opponent's attacks (after applying Weakness and Resistance), and your opponent's attacks and Abilities can't put damage counters on it.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="fbf09001-e3f8-5eda-9b50-3b0f5002656e",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MetalGoggles.Name",
    display_name="Metal Goggles",
    searchable_by=["Metal Goggles", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=195,
    set_code="SM9",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
