"""STUB: effect not implemented — do not guess mechanics.
Fairy Charm Dragon (SM8 #177): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - Prevent all damage done to the Fairy Pokémon this card is attached to by attacks from your opponent's Dragon Pokémon-GX and Dragon Pokémon-EX.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="f0acb0ae-1312-52d1-923d-c1ae1b9ffaf0",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FairyCharmDragon.Name",
    display_name="Fairy Charm Dragon",
    searchable_by=["Fairy Charm Dragon", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=177,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
