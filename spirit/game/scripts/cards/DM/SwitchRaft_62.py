"""STUB: effect not implemented — do not guess mechanics.
Switch Raft (DM #62): trainer effect stubbed.

Card text:
  - Switch your Active Water Pokémon with 1 of your Benched Pokémon. If you do, heal 30 damage from the Pokémon you moved to your Bench.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="09cc0b2d-be04-5aa3-804c-e300eb45ab0c",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SwitchRaft.Name",
    display_name="Switch Raft",
    searchable_by=["Switch Raft", "Item"],
    subtypes=["Item"],
    collector_number=62,
    set_code="DM",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
