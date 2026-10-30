"""STUB: effect not implemented — do not guess mechanics.
Balloon Berry (EX8 #84): trainer effect stubbed.

Card text:
  - Attach Balloon Berry to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. If that Pokémon is Knocked Out, discard this card.
  - As long as Balloon Berry is attached to a Pokémon, that Pokémon's Retreat Cost is 0. When this Pokémon retreats, discard Balloon Berry.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="9127027c-8219-5bfa-b861-203464b0e059",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BalloonBerry.Name",
    display_name="Balloon Berry",
    searchable_by=["Balloon Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=84,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
