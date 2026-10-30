"""STUB: effect not implemented — do not guess mechanics.
Protective Orb (EX10 #90): trainer effect stubbed.

Card text:
  - Attach Protective Orb to 1 of your Evolved Pokémon (excluding Pokémon-ex) that doesn't already have a Pokémon Tool attached to it. If the Pokémon Protective Orb is attached to is a Basic Pokémon or Pokémon-ex, discard Protective Orb.
  - As long as Protective Orb is attached to a Pokémon, that Pokémon has no Weakness.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="e27b6f6e-ca21-5763-bbd2-094792365342",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProtectiveOrb.Name",
    display_name="Protective Orb",
    searchable_by=["Protective Orb", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=90,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
