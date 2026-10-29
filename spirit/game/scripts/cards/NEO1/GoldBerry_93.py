"""STUB: effect not implemented — do not guess mechanics.
Gold Berry (NEO1 #93): trainer effect stubbed.

Card text:
  - Attach Gold Berry to 1 of your Pokémon that doesn't have a Pokémon Tool attached to it.
  - At any time between turns, if there are at least 4 damage counters on the Pokémon Gold Berry is attached to, you may remove 4 of them and discard Gold Berry. At the start of each turn, if there are at least 4 damage counters on the Pokémon Gold Berry is attached to, remove 4 of them and discard Gold Berry.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="5f5d9d4e-476f-56a0-8e63-c53791a6a19c",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GoldBerry.Name",
    display_name="Gold Berry",
    searchable_by=["Gold Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=93,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
