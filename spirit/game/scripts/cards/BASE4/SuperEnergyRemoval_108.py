"""STUB: effect not implemented — do not guess mechanics.
Super Energy Removal (BASE4 #108): trainer effect stubbed.

Card text:
  - Discard 1 Energy card attached to 1 of your own Pokémon in order to choose 1 of your opponent's Pokémon and up to 2 Energy cards attached to it. Discard those Energy cards.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d432f18b-0bce-5d88-bdff-fc4838071e09",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SuperEnergyRemoval.Name",
    display_name="Super Energy Removal",
    searchable_by=["Super Energy Removal"],
    subtypes=[],
    collector_number=108,
    set_code="BASE4",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
