"""STUB: effect not implemented — do not guess mechanics.
Moomoo Milk (SM8 #185): trainer effect stubbed.

Card text:
  - Choose 1 of your Pokémon, and then flip 2 coins. For each heads, heal 30 damage from that Pokémon.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="18c207d0-88ff-551a-a391-add93b936b6d",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MoomooMilk.Name",
    display_name="Moomoo Milk",
    searchable_by=["Moomoo Milk", "Item"],
    subtypes=["Item"],
    collector_number=185,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
