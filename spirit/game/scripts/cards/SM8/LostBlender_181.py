"""STUB: effect not implemented — do not guess mechanics.
Lost Blender (SM8 #181): trainer effect stubbed.

Card text:
  - Put 2 cards from your hand in the Lost Zone. If you do, draw a card.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="798bfab3-56f4-5135-ae07-45ae52e24f7e",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LostBlender.Name",
    display_name="Lost Blender",
    searchable_by=["Lost Blender", "Item"],
    subtypes=["Item"],
    collector_number=181,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
