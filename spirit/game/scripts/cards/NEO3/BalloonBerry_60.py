"""STUB: effect not implemented — do not guess mechanics.
Balloon Berry (NEO3 #60): trainer effect stubbed.

Card text:
  - Attach Balloon Berry to 1 of your Pokémon that doesn't have a Pokémon Tool attached to it.
  - When the Pokémon Balloon Berry is attached to retreats, discard Balloon Berry instead of discarding Energy cards.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="ff9325fa-57c2-59c4-a1dd-04098990c761",
    key="NEO3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BalloonBerry.Name",
    display_name="Balloon Berry",
    searchable_by=["Balloon Berry", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=60,
    set_code="NEO3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
