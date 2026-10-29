"""STUB: effect not implemented — do not guess mechanics.
Super Scoop Up (SM3 #166): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, put 1 of your Pokémon and all cards attached to it into your hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="38b6a143-0c08-5332-9763-2699e6c81e27",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=166,
    set_code="SM3",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
