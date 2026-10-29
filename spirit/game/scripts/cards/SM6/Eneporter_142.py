"""STUB: effect not implemented — do not guess mechanics.
Eneporter (SM6 #142): trainer effect stubbed.

Card text:
  - Move a Special Energy from 1 of your opponent's Pokémon to another of their Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="3cedc8b5-8c92-59a5-95f4-94853e06f4ed",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Eneporter.Name",
    display_name="Eneporter",
    searchable_by=["Eneporter", "Item"],
    subtypes=["Item"],
    collector_number=142,
    set_code="SM6",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
