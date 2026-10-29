"""STUB: effect not implemented — do not guess mechanics.
Water Memory (SM9 #157): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The Silvally-GX this card is attached to is a Water Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="bb508993-d0c7-55a3-9634-bbcb2834f7b1",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WaterMemory.Name",
    display_name="Water Memory",
    searchable_by=["Water Memory", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=157,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
