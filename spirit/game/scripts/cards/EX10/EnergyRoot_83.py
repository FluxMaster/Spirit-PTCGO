"""STUB: effect not implemented — do not guess mechanics.
Energy Root (EX10 #83): trainer effect stubbed.

Card text:
  - Attach Energy Root to 1 of your Pokémon (excluding Pokémon-ex and Pokémon that has Dark or an owner in its name) that doesn't already have a Pokémon Tool attached to it. If the Pokémon Energy Root is attached to is Pokémon-ex or has Dark or an owner in its name, discard Energy Root.
  - As long as Energy Root is attached to a Pokémon, that Pokémon gets +20 HP and can't use any Poké-Powers or Poké-Bodies.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="c3cebfb7-1434-535e-a670-7dcab2fc4d21",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRoot.Name",
    display_name="Energy Root",
    searchable_by=["Energy Root", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=83,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
