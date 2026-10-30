"""STUB: effect not implemented — do not guess mechanics.
Life Herb (EX6 #93): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, choose 1 of your Pokémon (excluding Pokémon-ex), and remove all Special Conditions and 6 damage counters from that Pokémon (all if there are less than 6).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="25f92163-6207-523b-83fc-4811270e30b4",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LifeHerb.Name",
    display_name="Life Herb",
    searchable_by=["Life Herb", "Item"],
    subtypes=["Item"],
    collector_number=93,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
