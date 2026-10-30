"""STUB: effect not implemented — do not guess mechanics.
Memory Berry (EX14 #80): trainer effect stubbed.

Card text:
  - Attach Memory Berry to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. If that Pokémon is Knocked Out, discard this card.
  - The Pokémon this card is attached to can use any attack from its Basic Pokémon or its Stage 1 Evolution card. (You still have to pay for that attack's Energy cost.) If that Pokémon attacks, discard this card at the end of the turn.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="bb62c9e2-7d57-58e3-93b6-de161ebf1d8c",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MemoryBerry.Name",
    display_name="Memory Berry",
    searchable_by=["Memory Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=80,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
