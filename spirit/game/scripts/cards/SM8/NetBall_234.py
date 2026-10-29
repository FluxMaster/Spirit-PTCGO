"""STUB: effect not implemented — do not guess mechanics.
Net Ball (SM8 #234): trainer effect stubbed.

Card text:
  - Search your deck for a Basic Grass Pokémon or a Grass Energy card, reveal it, and put it into your hand. Then, shuffle your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="890e0328-debc-58b4-ba61-808a59bf0516",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NetBall.Name",
    display_name="Net Ball",
    searchable_by=["Net Ball", "Item"],
    subtypes=["Item"],
    collector_number=234,
    set_code="SM8",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
