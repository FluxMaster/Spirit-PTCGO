"""STUB: effect not implemented — do not guess mechanics.
Beast Bringer (SM10 #229): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - If you have exactly 6 Prize cards remaining, and if your opponent's Active Pokémon-GX or Pokémon-EX is Knocked Out by damage from an attack of the Ultra Beast this card is attached to, take 1 more Prize card.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="83d5f1c8-103a-5aad-af36-0fc821c360f5",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeastBringer.Name",
    display_name="Beast Bringer",
    searchable_by=["Beast Bringer", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=229,
    set_code="SM10",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
