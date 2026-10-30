"""STUB: effect not implemented — do not guess mechanics.
Team Magma Belt (EX4 #81): trainer effect stubbed.

Card text:
  - Attach Team Magma Belt to 1 of your Pokémon with Team Magma in its name that doesn't already have a Pokémon Tool attached to it. If that Pokémon is Knocked Out, discard this card.
  - At any time between turns, if the Pokémon Team Magma Belt is attached to is your Active Pokémon, search your deck for a card that evolves from that Pokémon and put it on that Pokémon. (This counts as evolving that Pokémon.) Shuffle your deck afterward, then discard Team Magma Belt.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="d7e857d0-9148-532f-8e60-72576f99906e",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaBelt.Name",
    display_name="Team Magma Belt",
    searchable_by=["Team Magma Belt", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=81,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
