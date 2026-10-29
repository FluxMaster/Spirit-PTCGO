"""STUB: effect not implemented — do not guess mechanics.
Rainbow Brush (SM7 #141): trainer effect stubbed.

Card text:
  - Choose an Energy card attached to 1 of your Pokémon. Search your deck for a basic Energy card and switch it with that card. Shuffle the first Energy card into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e52193d6-c1c9-5bf1-910b-2786a41ef753",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RainbowBrush.Name",
    display_name="Rainbow Brush",
    searchable_by=["Rainbow Brush", "Item"],
    subtypes=["Item"],
    collector_number=141,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
