"""STUB: effect not implemented — do not guess mechanics.
Dashing Pouch (SM4 #92): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - If the Pokémon this card is attached to discards Energy for its Retreat Cost, put that Energy into your hand instead of the discard pile.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="12426934-c087-57bc-afef-a4042c424aed",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DashingPouch.Name",
    display_name="Dashing Pouch",
    searchable_by=["Dashing Pouch", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=92,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
