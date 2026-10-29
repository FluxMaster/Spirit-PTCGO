"""STUB: effect not implemented — do not guess mechanics.
Pal Pad (SM5 #132): trainer effect stubbed.

Card text:
  - Shuffle 2 Supporter cards from your discard pile into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="3fc95433-f1bc-5080-b3f9-36183a475eba",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PalPad.Name",
    display_name="Pal Pad",
    searchable_by=["Pal Pad", "Item"],
    subtypes=["Item"],
    collector_number=132,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
