"""STUB: effect not implemented — do not guess mechanics.
Oran Berry (EX1 #85): trainer effect stubbed.

Card text:
  - Attach Oran Berry to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. If that Pokémon is Knocked Out, discard this card.
  - At any time between turns, if the Pokémon this card is attached to has at least 2 damage counters on it, remove 2 damage counters from it. Then discard Oran Berry.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="6a4b0b44-0dd5-571e-9423-3a6f1f4e37d4",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.OranBerry.Name",
    display_name="Oran Berry",
    searchable_by=["Oran Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=85,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
