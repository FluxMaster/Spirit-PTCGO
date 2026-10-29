"""STUB: effect not implemented — do not guess mechanics.
Berry (NEO1 #99): trainer effect stubbed.

Card text:
  - Attach Berry to 1 of your Pokémon that doesn't have a Pokémon Tool attached to it.
  - At any time between turns, if there are at least 2 damage counters on the Pokémon Berry is attached to, you may remove 2 of them and discard Berry. At the start of each turn, if there are at least 2 damage counters on the Pokémon Berry is attached to, remove 2 of them and discard Berry.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="0c2ed99b-285a-594d-9459-83bf84e2db1f",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Berry.Name",
    display_name="Berry",
    searchable_by=["Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=99,
    set_code="NEO1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
