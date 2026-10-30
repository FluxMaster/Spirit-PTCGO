"""STUB: effect not implemented — do not guess mechanics.
Super Scoop Up (EX11 #100): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, return 1 of your Pokémon and all cards attached to it to your hand.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="78146353-4088-5ba3-a5a5-3b82330fc63c",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=100,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
