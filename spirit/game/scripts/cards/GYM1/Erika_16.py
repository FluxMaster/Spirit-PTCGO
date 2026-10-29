"""STUB: effect not implemented — do not guess mechanics.
Erika (GYM1 #16): trainer effect stubbed.

Card text:
  - You may draw up to 3 cards, then your opponent may draw up to 3 cards.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="c3978618-8737-5605-94d5-e09c82e3f262",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Erika.Name",
    display_name="Erika",
    searchable_by=["Erika"],
    subtypes=[],
    collector_number=16,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
