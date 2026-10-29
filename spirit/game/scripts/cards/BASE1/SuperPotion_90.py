"""STUB: effect not implemented — do not guess mechanics.
Super Potion (BASE1 #90): trainer effect stubbed.

Card text:
  - Discard 1 Energy card attached to your own Pokémon in order to remove up to 4 damage counters from that Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="aee1a71a-3df8-5067-b0cb-195ae1ab3724",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperPotion.Name",
    display_name="Super Potion",
    searchable_by=["Super Potion"],
    subtypes=[],
    collector_number=90,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
