"""STUB: effect not implemented — do not guess mechanics.
Grass Memory (SM9 #143): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The Silvally-GX this card is attached to is a Grass Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="de58d6a0-2a29-5daf-8613-9034f83579e3",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GrassMemory.Name",
    display_name="Grass Memory",
    searchable_by=["Grass Memory", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=143,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
