"""STUB: effect not implemented — do not guess mechanics.
Team Aqua Belt (EX4 #76): trainer effect stubbed.

Card text:
  - Attach Team Aqua Belt to 1 of your Pokémon with Team Aqua in its name that doesn't already have a Pokémon Tool attached to it. If that Pokémon is Knocked Out, discard this card.
  - At any time between turns, if the Pokémon Team Aqua Belt is attached to is your Active Pokémon, search your deck for a card that evolves from that Pokémon and put it on that Pokémon. (This counts as evolving that Pokémon.) Shuffle your deck afterward, then discard Team Aqua Belt.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="cd2fc041-274c-5f40-bbbb-df945207e758",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaBelt.Name",
    display_name="Team Aqua Belt",
    searchable_by=["Team Aqua Belt", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=76,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
