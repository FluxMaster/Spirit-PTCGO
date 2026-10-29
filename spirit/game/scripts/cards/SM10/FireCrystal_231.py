"""STUB: effect not implemented — do not guess mechanics.
Fire Crystal (SM10 #231): trainer effect stubbed.

Card text:
  - Put 3 Fire Energy cards from your discard pile into your hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="3e059737-81d7-5c70-89fb-9acba4c54819",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FireCrystal.Name",
    display_name="Fire Crystal",
    searchable_by=["Fire Crystal", "Item"],
    subtypes=["Item"],
    collector_number=231,
    set_code="SM10",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
