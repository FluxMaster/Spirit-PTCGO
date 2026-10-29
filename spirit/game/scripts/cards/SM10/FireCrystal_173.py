"""STUB: effect not implemented — do not guess mechanics.
Fire Crystal (SM10 #173): trainer effect stubbed.

Card text:
  - Put 3 Fire Energy cards from your discard pile into your hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="710d6432-b23e-5aa0-bfdf-56071c6bf6b3",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FireCrystal.Name",
    display_name="Fire Crystal",
    searchable_by=["Fire Crystal", "Item"],
    subtypes=["Item"],
    collector_number=173,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
