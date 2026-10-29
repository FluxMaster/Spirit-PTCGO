"""STUB: effect not implemented — do not guess mechanics.
Psychic Memory (SM4 #98): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The Silvally-GX this card is attached to is a Psychic Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="f9522309-7180-549a-89b2-c895b0f158dd",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PsychicMemory.Name",
    display_name="Psychic Memory",
    searchable_by=["Psychic Memory", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=98,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
