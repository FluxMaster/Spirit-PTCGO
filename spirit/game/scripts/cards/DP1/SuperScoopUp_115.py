"""STUB: effect not implemented — do not guess mechanics.
Super Scoop Up (DP1 #115): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, return 1 of your Pokémon and all cards attached to it to your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="70dc0081-0f41-557c-bc63-9fb42bce4a64",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=115,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
