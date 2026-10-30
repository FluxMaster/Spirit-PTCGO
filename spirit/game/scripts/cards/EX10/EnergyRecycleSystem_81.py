"""STUB: effect not implemented — do not guess mechanics.
Energy Recycle System (EX10 #81): trainer effect stubbed.

Card text:
  - Search your discard pile for basic Energy cards. You may either show 1 basic Energy card to your opponent and put it into your hand, or show 3 basic Energy cards to your opponent and shuffle them into your deck.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="63125fd1-a742-5c7b-b5a1-8b78cec0206d",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyRecycleSystem.Name",
    display_name="Energy Recycle System",
    searchable_by=["Energy Recycle System", "Item"],
    subtypes=["Item"],
    collector_number=81,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
