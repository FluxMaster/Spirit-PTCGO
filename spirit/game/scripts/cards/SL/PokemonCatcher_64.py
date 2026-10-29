"""STUB: effect not implemented — do not guess mechanics.
Pokémon Catcher (SL #64): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, switch 1 of your opponent's Benched Pokémon with their Active Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ff13f3cf-5e8c-58d0-baf5-683ab296b524",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonCatcher.Name",
    display_name="Pokémon Catcher",
    searchable_by=["Pok\u00e9mon Catcher", "Item"],
    subtypes=["Item"],
    collector_number=64,
    set_code="SL",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
