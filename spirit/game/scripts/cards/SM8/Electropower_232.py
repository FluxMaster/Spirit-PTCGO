"""STUB: effect not implemented — do not guess mechanics.
Electropower (SM8 #232): trainer effect stubbed.

Card text:
  - During this turn, your Lightning Pokémon's attacks do 30 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="7a21cce4-8939-5a11-b9d8-66f8ee0776bb",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Electropower.Name",
    display_name="Electropower",
    searchable_by=["Electropower", "Item"],
    subtypes=["Item"],
    collector_number=232,
    set_code="SM8",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
