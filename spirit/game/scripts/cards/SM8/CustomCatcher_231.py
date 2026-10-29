"""STUB: effect not implemented — do not guess mechanics.
Custom Catcher (SM8 #231): trainer effect stubbed.

Card text:
  - You may play 2 Custom Catcher cards at once.
• If you played 1 card, draw cards until you have 3 cards in your hand.
• If you played 2 cards, switch 1 of your opponent's Benched Pokémon with their Active Pokémon. (This effects works one time for 2 cards.)
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="af6f9c85-6eac-5492-83c8-46cc0089095f",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.CustomCatcher.Name",
    display_name="Custom Catcher",
    searchable_by=["Custom Catcher", "Item"],
    subtypes=["Item"],
    collector_number=231,
    set_code="SM8",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
