"""STUB: effect not implemented — do not guess mechanics.
Fairy Charm UB (SM9 #142): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Prevent all damage done to the Fairy Pokémon this card is attached to by attacks from your opponent's Ultra Beast Pokémon-GX and Ultra Beast Pokémon-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="69cc2e46-9d61-5ccf-8927-f5264056f8c5",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmUB.Name",
    display_name="Fairy Charm UB",
    searchable_by=["Fairy Charm UB", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=142,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
