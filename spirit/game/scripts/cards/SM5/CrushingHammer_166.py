"""STUB: effect not implemented — do not guess mechanics.
Crushing Hammer (SM5 #166): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, discard an Energy from 1 of your opponent's Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="adb6d1e9-6299-5b7f-9858-1741ca85655d",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CrushingHammer.Name",
    display_name="Crushing Hammer",
    searchable_by=["Crushing Hammer", "Item"],
    subtypes=["Item"],
    collector_number=166,
    set_code="SM5",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
