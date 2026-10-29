"""STUB: effect not implemented — do not guess mechanics.
Super Scoop Up (SL #66): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, put 1 of your Pokémon and all cards attached to it into your hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="46ef9ba8-5b5e-5c99-b96e-db9179f3887a",
    key="SL",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name",
    display_name="Super Scoop Up",
    searchable_by=["Super Scoop Up", "Item"],
    subtypes=["Item"],
    collector_number=66,
    set_code="SL",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
