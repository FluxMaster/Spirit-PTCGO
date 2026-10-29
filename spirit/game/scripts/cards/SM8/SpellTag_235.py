"""STUB: effect not implemented — do not guess mechanics.
Spell Tag (SM8 #235): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - When the Psychic Pokémon this card is attached to is Knocked Out by damage from an opponent's attack, put 4 damage counters on your opponent's Pokémon in any way you like.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="114a960f-9ed7-5db1-b480-0363f563bcea",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SpellTag.Name",
    display_name="Spell Tag",
    searchable_by=["Spell Tag", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=235,
    set_code="SM8",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
