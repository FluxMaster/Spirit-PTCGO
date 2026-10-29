"""STUB: effect not implemented — do not guess mechanics.
Net Ball (SM8 #187): trainer effect stubbed.

Card text:
  - Search your deck for a Basic Grass Pokémon or a Grass Energy card, reveal it, and put it into your hand. Then, shuffle your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="5e41116c-5c19-58bb-9c05-9fa66e3aa013",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NetBall.Name",
    display_name="Net Ball",
    searchable_by=["Net Ball", "Item"],
    subtypes=["Item"],
    collector_number=187,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
