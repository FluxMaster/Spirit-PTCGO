"""STUB: effect not implemented — do not guess mechanics.
Fairy Charm Grass (SM8 #174): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Prevent all damage done to the Fairy Pokémon this card is attached to by attacks from your opponent's Grass Pokémon-GX and Grass Pokémon-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="aea91199-90d4-5f3c-8319-74276b621455",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmGrass.Name",
    display_name="Fairy Charm Grass",
    searchable_by=["Fairy Charm Grass", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=174,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
