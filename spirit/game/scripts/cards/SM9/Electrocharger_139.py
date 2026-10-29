"""STUB: effect not implemented — do not guess mechanics.
Electrocharger (SM9 #139): trainer effect stubbed.

Card text:
  - Flip 2 coins. For each heads, shuffle an Electropower card from your discard pile into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="39e9f59b-c13e-5f3c-ae47-dc6d8d834dd3",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Electrocharger.Name",
    display_name="Electrocharger",
    searchable_by=["Electrocharger", "Item"],
    subtypes=["Item"],
    collector_number=139,
    set_code="SM9",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
