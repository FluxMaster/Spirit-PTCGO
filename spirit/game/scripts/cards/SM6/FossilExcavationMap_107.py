"""STUB: effect not implemented — do not guess mechanics.
Fossil Excavation Map (SM6 #107): trainer effect stubbed.

Card text:
  - Choose 1:
• Search your deck for an Unidentified Fossil card, reveal it, and put it into your hand. Then, shuffle your deck.
• Put an Unidentified Fossil card from your discard pile into your hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="6b7d0bfc-a78a-5fd6-9d2d-bf502534705e",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FossilExcavationMap.Name",
    display_name="Fossil Excavation Map",
    searchable_by=["Fossil Excavation Map", "Item"],
    subtypes=["Item"],
    collector_number=107,
    set_code="SM6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
