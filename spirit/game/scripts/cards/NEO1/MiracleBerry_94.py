"""STUB: effect not implemented — do not guess mechanics.
Miracle Berry (NEO1 #94): trainer effect stubbed.

Card text:
  - Attach Miracle Berry to 1 of your Pokémon that doesn't have a Pokémon Tool attached to it.
  - At any time between turns, if the Pokémon Miracle Berry is attached to is Asleep, Confused, Paralyzed, or Poisoned, you may remove all those effects from that Pokémon and discard Miracle Berry. At the start of each turn, if the Pokémon Miracle Berry is attached to is Asleep, Confused, Paralyzed, or Poisoned, remove all of those effects from that Pokémon and discard Miracle Berry.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="a31fc863-83ce-58d4-a71d-8799b86444a3",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MiracleBerry.Name",
    display_name="Miracle Berry",
    searchable_by=["Miracle Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=94,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
