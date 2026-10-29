"""STUB: effect not implemented — do not guess mechanics.
Multi Switch (SM2 #129): trainer effect stubbed.

Card text:
  - Move an Energy from 1 of your Benched Pokémon to your Active Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="0c698d08-3e32-57c7-b9ef-f490af9b53e7",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MultiSwitch.Name",
    display_name="Multi Switch",
    searchable_by=["Multi Switch", "Item"],
    subtypes=["Item"],
    collector_number=129,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
