"""STUB: effect not implemented — do not guess mechanics.
Energy Removal 2 (EX6 #89): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, choose 1 Energy card attached to 1 of your opponent's Pokémon and discard it.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e7b03854-ca7c-585a-b33b-78e45995c8b2",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRemoval2.Name",
    display_name="Energy Removal 2",
    searchable_by=["Energy Removal 2", "Item"],
    subtypes=["Item"],
    collector_number=89,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
