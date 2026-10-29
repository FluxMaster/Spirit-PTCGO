"""STUB: effect not implemented — do not guess mechanics.
Adventure Bag (SM8 #228): trainer effect stubbed.

Card text:
  - Search your deck for up to 2 Pokémon Tool cards, reveal them, and put them into your hand. Then, shuffle your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="31a033b8-abc4-5eb5-b8ee-db577981eaa5",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AdventureBag.Name",
    display_name="Adventure Bag",
    searchable_by=["Adventure Bag", "Item"],
    subtypes=["Item"],
    collector_number=228,
    set_code="SM8",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
