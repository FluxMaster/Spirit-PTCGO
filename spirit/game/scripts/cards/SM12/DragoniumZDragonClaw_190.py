"""STUB: effect not implemented — do not guess mechanics.
Dragonium Z: Dragon Claw (SM12 #190): trainer effect stubbed.

Card text:
  - Attach a Pokémon Tool to 1 of your Pokémon that doesn't already have a Pokémon Tool attached to it.
  - If the Pokémon this card is attached to has the Dragon Claw attack, it can use the GX attack on this card. (You still need the necessary Energy to use this attack.)
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import PokemonToolCardDef, unimplemented
from spirit.game.attributes import Rarities

card = PokemonToolCardDef(
    guid="ea7c61e1-4083-504f-b87a-1f3f72395048",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DragoniumZDragonClaw.Name",
    display_name="Dragonium Z: Dragon Claw",
    searchable_by=["Dragonium Z: Dragon Claw", "Pok\u00e9mon Tool"],
    subtypes=["Pok\u00e9mon Tool"],
    collector_number=190,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
