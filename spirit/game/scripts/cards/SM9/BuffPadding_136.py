"""STUB: effect not implemented — do not guess mechanics.
Buff Padding (SM9 #136): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - If the Pokémon this card is attached to has a Retreat Cost of exactly 4, it gets +50 HP.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="b7ced02f-ca3b-5aaa-a021-a9a26ba63f12",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BuffPadding.Name",
    display_name="Buff Padding",
    searchable_by=["Buff Padding", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=136,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
