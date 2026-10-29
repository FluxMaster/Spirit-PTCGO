"""STUB: effect not implemented — do not guess mechanics.
Fiery Flint (DM #60a): trainer effect stubbed.

Card text:
  - You can play this card only if you discard 2 other cards from your hand.
  - Search your deck for up to 4 Fire Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="11a64d81-279d-50cb-b505-2c853702f65c",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FieryFlint.Name",
    display_name="Fiery Flint",
    searchable_by=["Fiery Flint", "Item"],
    subtypes=["Item"],
    collector_number=80,
    set_code="DM",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
