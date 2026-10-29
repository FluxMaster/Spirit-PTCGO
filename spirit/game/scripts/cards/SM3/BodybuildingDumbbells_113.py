"""STUB: effect not implemented — do not guess mechanics.
Bodybuilding Dumbbells (SM3 #113): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The Stage 1 Pokémon this card is attached to gets +40 HP.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="cf91b818-3007-5cb6-ae83-b961cf0135b2",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BodybuildingDumbbells.Name",
    display_name="Bodybuilding Dumbbells",
    searchable_by=["Bodybuilding Dumbbells", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=113,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
