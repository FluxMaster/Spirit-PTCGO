"""STUB: effect not implemented — do not guess mechanics.
Switch (SM7 #147): trainer effect stubbed.

Card text:
  - Switch your Active Pokémon with 1 of your Benched Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="3a844764-8c54-5957-b576-875930501126",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Switch.Name",
    display_name="Switch",
    searchable_by=["Switch", "Item"],
    subtypes=["Item"],
    collector_number=147,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
