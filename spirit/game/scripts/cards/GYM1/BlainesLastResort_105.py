"""STUB: effect not implemented — do not guess mechanics.
Blaine's Last Resort (GYM1 #105): trainer effect stubbed.

Card text:
  - You can't play this card if you have any cards in your hand other than Blaine's Last Resort. Show your hand to your opponent, then draw 5 cards.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="bee093f9-1659-5487-bddb-424a66bb09cd",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BlainesLastResort.Name",
    display_name="Blaine's Last Resort",
    searchable_by=["Blaine's Last Resort"],
    subtypes=[],
    collector_number=105,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
