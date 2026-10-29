"""STUB: effect not implemented — do not guess mechanics.
Focus Band (NEO1 #86): trainer effect stubbed.

Card text:
  - Attach Focus Band to 1 of your Pokémon that doesn't have a Pokémon Tool attached to it.
  - If the Pokémon Focus Band is attached to would be Knocked Out by your opponent's attack, flip a coin. If heads, that Pokémon is not Knocked Out and its remaining HP become 10 instead. Then, discard Focus Band.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="eb76395f-e6b4-54b2-b5f9-052d16fa9b94",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FocusBand.Name",
    display_name="Focus Band",
    searchable_by=["Focus Band", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=86,
    set_code="NEO1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
