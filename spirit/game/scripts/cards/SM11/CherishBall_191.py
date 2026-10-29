"""STUB: effect not implemented — do not guess mechanics.
Cherish Ball (SM11 #191): trainer effect stubbed.

Card text:
  - Search your deck for a Pokémon-GX, reveal it, and put it into your hand. Then, shuffle your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e4c3219c-86a4-5916-b99c-b1f96a23f8a8",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CherishBall.Name",
    display_name="Cherish Ball",
    searchable_by=["Cherish Ball", "Item"],
    subtypes=["Item"],
    collector_number=191,
    set_code="SM11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
