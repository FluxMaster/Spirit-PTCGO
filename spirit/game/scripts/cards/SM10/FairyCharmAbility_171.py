"""STUB: effect not implemented — do not guess mechanics.
Fairy Charm Ability (SM10 #171): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Prevent all damage done to the Fairy Pokémon this card is attached to by attacks from your opponent's Pokémon-GX and Pokémon-EX that have Abilities.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="e55c142b-4b16-53ba-9e76-27371d728790",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmAbility.Name",
    display_name="Fairy Charm Ability",
    searchable_by=["Fairy Charm Ability", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=171,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
