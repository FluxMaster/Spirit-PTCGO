"""STUB: effect not implemented — do not guess mechanics.
Energy Recycle System (SM7 #128): trainer effect stubbed.

Card text:
  - Choose 1:
• Put a basic Energy card from your discard pile into your hand.
• Shuffle 3 basic Energy cards from your discard pile into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="5d36af85-9b3d-50d4-9078-07db64b03353",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRecycleSystem.Name",
    display_name="Energy Recycle System",
    searchable_by=["Energy Recycle System", "Item"],
    subtypes=["Item"],
    collector_number=128,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
