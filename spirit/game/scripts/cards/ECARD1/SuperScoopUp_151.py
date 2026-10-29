"""STUB: effect not implemented — do not guess mechanics.
Super Scoop Up (ECARD1 #151): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, return 1 of your Pokémon and all cards attached to it to your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="bcae4fe8-399d-52d0-913f-94576ffb37c0",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up"],
    subtypes=[],
    collector_number=151,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
