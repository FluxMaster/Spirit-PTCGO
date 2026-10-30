"""STUB: effect not implemented — do not guess mechanics.
Curse Powder (EX10 #80): trainer effect stubbed.

Card text:
  - Attach Curse Powder to 1 of your Evolved Pokémon (excluding Pokémon-ex) that doesn't already have a Pokémon Tool attached to it. If the Pokémon Curse Powder is attached to is a Basic Pokémon or Pokémon-ex, discard Curse Powder.
  - If the Pokémon that Curse Powder is attached to is your Active Pokémon and is Knocked Out by damage from an opponent's attack, put 3 damage counters on the Attacking Pokémon.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="0348afb2-4d7c-5ab4-bcb8-1d9b7c130515",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CursePowder.Name",
    display_name="Curse Powder",
    searchable_by=["Curse Powder", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=80,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
