"""STUB: effect not implemented — do not guess mechanics.
Secret Mission (GYM1 #118): trainer effect stubbed.

Card text:
  - Look at your opponent's hand. Then, you may discard as many other cards as you want from your hand and draw that many cards.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="2052ce18-9aff-51a7-aeb8-a36dd65d6d56",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SecretMission.Name",
    display_name="Secret Mission",
    searchable_by=["Secret Mission"],
    subtypes=[],
    collector_number=118,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
