"""STUB: effect not implemented — do not guess mechanics.
Escape Board (SM5 #122): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The Retreat Cost of the Pokémon this card is attached to is Colorless less, and it can retreat even if it's Asleep or Paralyzed.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="fc22b6a2-1070-5011-be88-374afbfae4bc",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EscapeBoard.Name",
    display_name="Escape Board",
    searchable_by=["Escape Board", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=122,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
