"""STUB: effect not implemented — do not guess mechanics.
Fervor (GYM2 #124): trainer effect stubbed.

Card text:
  - Show the top 3 cards of your deck to all players. Put any Fire Energy cards there into your hand and discard the rest.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="952e2151-0c0c-5086-8a5d-323e6e1cdc2a",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fervor.Name",
    display_name="Fervor",
    searchable_by=["Fervor"],
    subtypes=[],
    collector_number=124,
    set_code="GYM2",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
