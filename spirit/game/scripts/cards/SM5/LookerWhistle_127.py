"""STUB: effect not implemented — do not guess mechanics.
Looker Whistle (SM5 #127): trainer effect stubbed.

Card text:
  - Search your deck for up to 2 cards named Looker, reveal them, and put them into your hand. Then, shuffle your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="be2917bb-9f22-5f45-9c31-37495b84cc06",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LookerWhistle.Name",
    display_name="Looker Whistle",
    searchable_by=["Looker Whistle", "Item"],
    subtypes=["Item"],
    collector_number=127,
    set_code="SM5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
