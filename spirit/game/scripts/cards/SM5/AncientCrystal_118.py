"""STUB: effect not implemented — do not guess mechanics.
Ancient Crystal (SM5 #118): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - The Regirock, Regice, Registeel, or Regigigas this card is attached to takes 30 less damage from your opponent's attacks (after applying Weakness and Resistance).
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="3e83a386-39a7-5482-82bb-5a651fe574c6",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AncientCrystal.Name",
    display_name="Ancient Crystal",
    searchable_by=["Ancient Crystal", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=118,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
