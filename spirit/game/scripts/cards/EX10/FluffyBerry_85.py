"""STUB: effect not implemented — do not guess mechanics.
Fluffy Berry (EX10 #85): trainer effect stubbed.

Card text:
  - Attach Fluffy Berry to 1 of your Pokémon (excluding Pokémon-ex and Pokémon that has Dark or an owner in its name) that doesn't already have a Pokémon Tool attached to it. If the Pokémon Fluffy Berry is attached to is Pokémon-ex or has Dark or an owner in its name, discard Fluffy Berry.
  - As long as Fluffy Berry is attached to a Pokémon, that Pokémon's Retreat Cost is 0.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="a3bb14d9-db24-5766-88e3-222cd39b1fb6",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FluffyBerry.Name",
    display_name="Fluffy Berry",
    searchable_by=["Fluffy Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=85,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
