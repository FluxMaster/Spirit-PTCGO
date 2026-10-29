"""STUB: effect not implemented — do not guess mechanics.
Energy Recycler (SM6 #143): trainer effect stubbed.

Card text:
  - Shuffle 5 basic Energy cards from your discard pile into your deck.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="522c6d24-1020-5d70-951e-41ae92eaf0d0",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRecycler.Name",
    display_name="Energy Recycler",
    searchable_by=["Energy Recycler", "Item"],
    subtypes=["Item"],
    collector_number=143,
    set_code="SM6",
    rarity=Rarities.RareSecret,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
