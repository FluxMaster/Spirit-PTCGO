"""STUB: effect not implemented — do not guess mechanics.
Beast Ring (SM6 #102a): trainer effect stubbed.

Card text:
  - You can play this card only if your opponent has exactly 3 or 4 Prize cards remaining.
  - Search your deck for up to 2 basic Energy cards and attach them to 1 of your Ultra Beasts. Then, shuffle your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="202fb962-9248-5fc1-b227-36958fc09560",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BeastRing.Name",
    display_name="Beast Ring",
    searchable_by=["Beast Ring", "Item"],
    subtypes=["Item"],
    collector_number=148,
    set_code="SM6",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
