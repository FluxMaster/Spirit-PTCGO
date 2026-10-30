"""STUB: effect not implemented — do not guess mechanics.
Quick Ball (DP2 #114): trainer effect stubbed.

Card text:
  - Reveal cards from your deck until you reveal a Pokémon. Show that Pokémon to your opponent and put it into your hand. Shuffle the other revealed cards back into your deck. (If you don't reveal a Pokémon, shuffle all the revealed cards back into your deck.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="5f810ad0-d313-5637-9e24-dce7b700c9fd",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.QuickBall.Name",
    display_name="Quick Ball",
    searchable_by=["Quick Ball", "Item"],
    subtypes=["Item"],
    collector_number=114,
    set_code="DP2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
