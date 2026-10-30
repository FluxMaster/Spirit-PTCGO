"""STUB: effect not implemented — do not guess mechanics.
Night Maintenance (POP8 #9): trainer effect stubbed.

Card text:
  - Search your discard pile for up to 3 in any combination of Pokémon and basic Energy cards. Show them to your opponent and shuffle them into your deck.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="374c81d2-1510-53cc-9a38-c8e79ccb3896",
    key="POP8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightMaintenance.Name",
    display_name="Night Maintenance",
    searchable_by=["Night Maintenance", "Item"],
    subtypes=["Item"],
    collector_number=9,
    set_code="POP8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
