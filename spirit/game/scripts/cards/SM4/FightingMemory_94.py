"""STUB: effect not implemented — do not guess mechanics.
Fighting Memory (SM4 #94): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The Silvally-GX this card is attached to is a Fighting Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="d246a228-e265-54ee-a7e9-b3bd6884945e",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FightingMemory.Name",
    display_name="Fighting Memory",
    searchable_by=["Fighting Memory", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=94,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
