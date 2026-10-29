"""STUB: effect not implemented — do not guess mechanics.
Super Potion (BASE4 #117): trainer effect stubbed.

Card text:
  - Discard 1 Energy card attached to 1 of your own Pokémon in order to remove up to 4 damage counters from that Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="f7d475d4-7947-5aa8-b375-59f37a015e42",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperPotion.Name",
    display_name="Super Potion",
    searchable_by=["Super Potion"],
    subtypes=[],
    collector_number=117,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
