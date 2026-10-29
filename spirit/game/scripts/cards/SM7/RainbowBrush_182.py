"""STUB: effect not implemented — do not guess mechanics.
Rainbow Brush (SM7 #182): trainer effect stubbed.

Card text:
  - Choose an Energy card attached to 1 of your Pokémon. Search your deck for a basic Energy card and switch it with that card. Shuffle the first Energy card into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="fa9c4885-6550-5be3-a9a4-fb34bdb48261",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RainbowBrush.Name",
    display_name="Rainbow Brush",
    searchable_by=["Rainbow Brush", "Item"],
    subtypes=["Item"],
    collector_number=182,
    set_code="SM7",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
