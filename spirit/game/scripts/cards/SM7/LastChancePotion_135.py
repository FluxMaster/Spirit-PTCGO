"""STUB: effect not implemented — do not guess mechanics.
Last Chance Potion (SM7 #135): trainer effect stubbed.

Card text:
  - Heal 120 damage from 1 of your Pokémon that has 30 HP or less remaining.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ae195811-c19a-598c-97b5-c879564382f6",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LastChancePotion.Name",
    display_name="Last Chance Potion",
    searchable_by=["Last Chance Potion", "Item"],
    subtypes=["Item"],
    collector_number=135,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
