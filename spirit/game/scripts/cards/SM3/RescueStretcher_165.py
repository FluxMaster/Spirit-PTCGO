"""STUB: effect not implemented — do not guess mechanics.
Rescue Stretcher (SM3 #165): trainer effect stubbed.

Card text:
  - Choose 1:
• Put a Pokémon from your discard pile into your hand.
• Shuffle 3 Pokémon from your discard pile into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="653e090e-d8be-5477-b622-30f83c5e6d06",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RescueStretcher.Name",
    display_name="Rescue Stretcher",
    searchable_by=["Rescue Stretcher", "Item"],
    subtypes=["Item"],
    collector_number=165,
    set_code="SM3",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
