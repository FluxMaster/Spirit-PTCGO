"""STUB: effect not implemented — do not guess mechanics.
Counterattack Claws (NEO4 #97): trainer effect stubbed.

Card text:
  - Attach Counterattack Claws to 1 of your Pokémon that doesn't have a Pokémon Tool attached to it.
  - During your opponent's turn, if the Pokémon Counterattack Claws is attached to is your Active Pokémon and an opponent's attack damages it (even if it is Knocked Out), flip a coin. If heads, put 2 damage counters on the Defending Pokémon. Then, discard Counterattack Claws.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="7dd63a07-5714-5b3d-9cab-c7c9b3519ece",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CounterattackClaws.Name",
    display_name="Counterattack Claws",
    searchable_by=["Counterattack Claws", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=97,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
