"""STUB: effect not implemented — do not guess mechanics.
Fairy Charm Lightning (SM10 #172): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Prevent all damage done to the Fairy Pokémon this card is attached to by attacks from your opponent's Lightning Pokémon-GX and Lightning Pokémon-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="bf0cb66a-2a98-516e-b038-bd443a6bfa7c",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmLightning.Name",
    display_name="Fairy Charm Lightning",
    searchable_by=["Fairy Charm Lightning", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=172,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
