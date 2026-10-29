"""STUB: effect not implemented — do not guess mechanics.
Counter Catcher (SM4 #120): trainer effect stubbed.

Card text:
  - You can play this card only if you have more Prize cards remaining than your opponent.
  - Switch 1 of your opponent's Benched Pokémon with their Active Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="8f9c9ca5-b3b6-5388-a3c6-651ee30c3d0b",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CounterCatcher.Name",
    display_name="Counter Catcher",
    searchable_by=["Counter Catcher", "Item"],
    subtypes=["Item"],
    collector_number=120,
    set_code="SM4",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
