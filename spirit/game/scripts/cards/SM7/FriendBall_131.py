"""STUB: effect not implemented — do not guess mechanics.
Friend Ball (SM7 #131): trainer effect stubbed.

Card text:
  - Search your deck for a Pokémon with the same type as 1 of your opponent's Pokémon in play, reveal it, and put it into your hand. Then, shuffle your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="37bc31bf-b9da-5c15-b5bf-f8e0d25aead8",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FriendBall.Name",
    display_name="Friend Ball",
    searchable_by=["Friend Ball", "Item"],
    subtypes=["Item"],
    collector_number=131,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
