"""STUB: effect not implemented — do not guess mechanics.
Switch Raft (DM #77): trainer effect stubbed.

Card text:
  - Switch your Active Water Pokémon with 1 of your Benched Pokémon. If you do, heal 30 damage from the Pokémon you moved to your Bench.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="2ed35178-8ed0-5430-a25a-0248454daed4",
    key="DM",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SwitchRaft.Name",
    display_name="Switch Raft",
    searchable_by=["Switch Raft", "Item"],
    subtypes=["Item"],
    collector_number=77,
    set_code="DM",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
