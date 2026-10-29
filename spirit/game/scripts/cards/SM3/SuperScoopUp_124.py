"""STUB: effect not implemented — do not guess mechanics.
Super Scoop Up (SM3 #124): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, put 1 of your Pokémon and all cards attached to it into your hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d9469aa4-6859-537a-9dae-50ca13a6f394",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=124,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
