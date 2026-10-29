"""STUB: effect not implemented — do not guess mechanics.
Super Energy Removal (BASE1 #79): trainer effect stubbed.

Card text:
  - Discard 1 Energy card attached to 1 of your Pokémon in order to choose 1 of your opponent's Pokémon and up to 2 Energy cards attached to it. Discard those Energy cards.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d6fb7dd9-912b-5b19-b73e-7cd907c300ac",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperEnergyRemoval.Name",
    display_name="Super Energy Removal",
    searchable_by=["Super Energy Removal"],
    subtypes=[],
    collector_number=79,
    set_code="BASE1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
