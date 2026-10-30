"""STUB: effect not implemented — do not guess mechanics.
Energy Removal 2 (EX10 #82): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, choose 1 Energy card attached to 1 of your opponent's Pokémon and discard it.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="4cbfcff4-9545-574a-838a-42abcaae05dd",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRemoval2.Name",
    display_name="Energy Removal 2",
    searchable_by=["Energy Removal 2", "Item"],
    subtypes=["Item"],
    collector_number=82,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
