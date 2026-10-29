"""STUB: effect not implemented — do not guess mechanics.
Eneporter (SM6 #106): trainer effect stubbed.

Card text:
  - Move a Special Energy from 1 of your opponent's Pokémon to another of their Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e4d8a65f-5efa-58de-97f0-f0528cbe0716",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Eneporter.Name",
    display_name="Eneporter",
    searchable_by=["Eneporter", "Item"],
    subtypes=["Item"],
    collector_number=106,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
