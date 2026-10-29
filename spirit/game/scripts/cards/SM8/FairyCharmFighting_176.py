"""STUB: effect not implemented — do not guess mechanics.
Fairy Charm Fighting (SM8 #176): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Prevent all damage done to the Fairy Pokémon this card is attached to by attacks from your opponent's Fighting Pokémon-GX and Fighting Pokémon-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="d593bdd3-d911-5f18-a563-8b982abb51e9",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmFighting.Name",
    display_name="Fairy Charm Fighting",
    searchable_by=["Fairy Charm Fighting", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=176,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
