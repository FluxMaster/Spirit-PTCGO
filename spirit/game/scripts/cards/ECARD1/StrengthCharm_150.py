"""STUB: effect not implemented — do not guess mechanics.
Strength Charm (ECARD1 #150): trainer effect stubbed.

Card text:
  - Attach Strength Charm to 1 of your Pokémon that doesn't have a Pokémon Tool attached to it.
  - Whenever an attack from the Pokémon that Strength Charm is attached to does damage (after applying Weakness and Resistance), the attack does 10 more damage. At the end of your turn in which this happens, discard Strength Charm.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="a989eae3-3ea3-5064-8f47-1d210c31dd17",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StrengthCharm.Name",
    display_name="Strength Charm",
    searchable_by=["Strength Charm", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=150,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
