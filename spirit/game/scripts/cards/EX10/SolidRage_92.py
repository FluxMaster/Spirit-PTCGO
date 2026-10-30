"""STUB: effect not implemented — do not guess mechanics.
Solid Rage (EX10 #92): trainer effect stubbed.

Card text:
  - Attach Solid Rage to 1 of your Evolved Pokémon (excluding Pokémon-ex) that doesn't already have a Pokémon Tool attached to it. If the Pokémon Solid Rage is attached to is a Basic Pokémon or Pokémon-ex, discard Solid Rage.
  - If you have more Prize cards left than your opponent, the Pokémon that Solid Rage is attached to does 20 more damage to the Active Pokémon (before applying Weakness and Resistance).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="c165450d-d3ce-5775-b79c-09998c5c22dd",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SolidRage.Name",
    display_name="Solid Rage",
    searchable_by=["Solid Rage", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=92,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
