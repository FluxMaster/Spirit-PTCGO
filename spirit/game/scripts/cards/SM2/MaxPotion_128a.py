"""STUB: effect not implemented — do not guess mechanics.
Max Potion (SM2 #128a): trainer effect stubbed.

Card text:
  - Heal all damage from 1 of your Pokémon. If you do, discard all Energy from that Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="17eebe32-6e11-5f1b-95c3-b6073cd4322b",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MaxPotion.Name",
    display_name="Max Potion",
    searchable_by=["Max Potion", "Item"],
    subtypes=["Item"],
    collector_number=178,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
