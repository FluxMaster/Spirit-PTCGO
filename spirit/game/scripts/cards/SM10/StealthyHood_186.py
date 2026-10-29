"""STUB: effect not implemented — do not guess mechanics.
Stealthy Hood (SM10 #186): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Prevent all effects of your opponent's Abilities done to the Pokémon this card is attached to. Remove any such existing effects.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="54bb7825-24ff-5e2d-bc5f-48985460adc4",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StealthyHood.Name",
    display_name="Stealthy Hood",
    searchable_by=["Stealthy Hood", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=186,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
