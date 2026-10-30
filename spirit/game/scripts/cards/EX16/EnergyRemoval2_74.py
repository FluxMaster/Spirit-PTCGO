"""STUB: effect not implemented — do not guess mechanics.
Energy Removal 2 (EX16 #74): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, choose 1 Energy card attached to 1 of your opponent's Pokémon and discard it.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="3afde8ac-a739-5561-9ec9-a302835b8e78",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRemoval2.Name",
    display_name="Energy Removal 2",
    searchable_by=["Energy Removal 2", "Item"],
    subtypes=["Item"],
    collector_number=74,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
