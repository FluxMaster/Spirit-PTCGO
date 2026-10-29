"""STUB: effect not implemented — do not guess mechanics.
Super Scoop Up (NEO1 #98): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, return 1 of your Pokémon and all cards attached to it to your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="48e9afb5-a38e-5879-a319-3a0023a79142",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up"],
    subtypes=[],
    collector_number=98,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
