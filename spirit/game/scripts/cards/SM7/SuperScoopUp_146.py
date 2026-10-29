"""STUB: effect not implemented — do not guess mechanics.
Super Scoop Up (SM7 #146): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, put 1 of your Pokémon and all cards attached to it into your hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="a632180d-16d5-587a-baae-e58e082150ba",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=146,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
