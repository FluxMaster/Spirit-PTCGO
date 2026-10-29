"""STUB: effect not implemented — do not guess mechanics.
Fire Memory (SM5 #123): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The Silvally-GX this card is attached to is a Fire Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="8afdad31-00e1-5bda-8783-d78c6d984f70",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FireMemory.Name",
    display_name="Fire Memory",
    searchable_by=["Fire Memory", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=123,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
