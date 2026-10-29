"""STUB: effect not implemented — do not guess mechanics.
Wishful Baton (SM4 #121): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - If the Pokémon this card is attached to is your Active Pokémon and is Knocked Out by damage from an opponent's attack, move up to 3 basic Energy cards from that Pokémon to 1 of your Benched Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="a105c6b0-4c0c-5732-a910-1b96b0b78c39",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.WishfulBaton.Name",
    display_name="Wishful Baton",
    searchable_by=["Wishful Baton", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=121,
    set_code="SM4",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
