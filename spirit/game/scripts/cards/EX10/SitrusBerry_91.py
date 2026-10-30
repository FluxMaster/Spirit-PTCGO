"""STUB: effect not implemented — do not guess mechanics.
Sitrus Berry (EX10 #91): trainer effect stubbed.

Card text:
  - Attach Sitrus Berry to 1 of your Pokémon (excluding Pokémon-ex and Pokémon that has Dark or an owner in its name) that doesn't already have a Pokémon Tool attached to it. If the Pokémon Sitrus Berry is attached to is Pokémon-ex or has Dark or an owner in its name, discard Sitrus Berry.
  - At any time between turns, if the Pokémon this card is attached to has at least 3 damage counters on it, remove 3 damage counters from it. Then, discard Sitrus Berry.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="87854b57-1540-5037-b0e6-9cd44286a79c",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SitrusBerry.Name",
    display_name="Sitrus Berry",
    searchable_by=["Sitrus Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=91,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
