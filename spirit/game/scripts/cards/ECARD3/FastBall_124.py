"""STUB: effect not implemented — do not guess mechanics.
Fast Ball (ECARD3 #124): trainer effect stubbed.

Card text:
  - Reveal cards from your deck until you reveal an Evolution card. Show that card to your opponent and put it into your hand. Shuffle the other revealed cards into your deck. (If you don't reveal an Evolution card, shuffle all the revealed cards back into your deck.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b061d93d-7948-5f3f-9d2b-9528b82c0ad1",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FastBall.Name",
    display_name="Fast Ball",
    searchable_by=["Fast Ball"],
    subtypes=[],
    collector_number=124,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
