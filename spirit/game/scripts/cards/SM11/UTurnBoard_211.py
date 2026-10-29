"""STUB: effect not implemented — do not guess mechanics.
U-Turn Board (SM11 #211): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The Retreat Cost of the Pokémon this card is attached to is Colorless less.
  - If this card is discarded from play, put it into your hand instead of the discard pile.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="b147176c-6cc4-5ca0-83ec-2758185bf986",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UTurnBoard.Name",
    display_name="U-Turn Board",
    searchable_by=["U-Turn Board", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=211,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
