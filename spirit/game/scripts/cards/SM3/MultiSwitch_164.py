"""STUB: effect not implemented — do not guess mechanics.
Multi Switch (SM3 #164): trainer effect stubbed.

Card text:
  - Move an Energy from 1 of your Benched Pokémon to your Active Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="cb41a083-4781-5f35-b326-c45f1062f26d",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MultiSwitch.Name",
    display_name="Multi Switch",
    searchable_by=["Multi Switch", "Item"],
    subtypes=["Item"],
    collector_number=164,
    set_code="SM3",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
