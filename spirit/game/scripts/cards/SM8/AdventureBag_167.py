"""STUB: effect not implemented — do not guess mechanics.
Adventure Bag (SM8 #167): trainer effect stubbed.

Card text:
  - Search your deck for up to 2 Pokémon Tool cards, reveal them, and put them into your hand. Then, shuffle your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="5767eea9-0589-5ace-b7de-4fb230fa6a06",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.AdventureBag.Name",
    display_name="Adventure Bag",
    searchable_by=["Adventure Bag", "Item"],
    subtypes=["Item"],
    collector_number=167,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
