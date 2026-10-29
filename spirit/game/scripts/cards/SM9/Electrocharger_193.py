"""STUB: effect not implemented — do not guess mechanics.
Electrocharger (SM9 #193): trainer effect stubbed.

Card text:
  - Flip 2 coins. For each heads, shuffle an Electropower card from your discard pile into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="78af3a11-93d0-541a-a3ac-5c7b59eda215",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Electrocharger.Name",
    display_name="Electrocharger",
    searchable_by=["Electrocharger", "Item"],
    subtypes=["Item"],
    collector_number=193,
    set_code="SM9",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
