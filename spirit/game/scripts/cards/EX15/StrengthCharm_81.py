"""STUB: effect not implemented — do not guess mechanics.
Strength Charm (EX15 #81): trainer effect stubbed.

Card text:
  - Attach Strength Charm to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it. If that Pokémon is Knocked Out, discard this card.
  - Whenever an attack from the Pokémon that Strength Charm is attached to does damage to the Active Pokémon, this attack does 10 more damage (before applying Weakness and Resistance). Discard Strength Charm at the end of the turn in which this Pokémon attacks.
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="60bb2ef7-569c-5a4e-9a75-4c15b17ddcd4",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StrengthCharm.Name",
    display_name="Strength Charm",
    searchable_by=["Strength Charm", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=81,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
