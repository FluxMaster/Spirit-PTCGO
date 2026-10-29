"""STUB: effect not implemented — do not guess mechanics.
Beast Bringer (SM10 #164): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - If you have exactly 6 Prize cards remaining, and if your opponent's Active Pokémon-GX or Pokémon-EX is Knocked Out by damage from an attack of the Ultra Beast this card is attached to, take 1 more Prize card.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="46315776-88a1-5d3a-93dc-43ae9ecb11d2",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeastBringer.Name",
    display_name="Beast Bringer",
    searchable_by=["Beast Bringer", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=164,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
