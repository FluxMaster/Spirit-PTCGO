"""STUB: effect not implemented — do not guess mechanics.
Life Herb (EX5 #90): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, choose 1 of your Pokémon (excluding Pokémon-ex). Remove all Special Conditions and 6 damage counters from that Pokémon (all if there are less than 6).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="daa3103a-db7f-5247-81c6-da2c40e1b582",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LifeHerb.Name",
    display_name="Life Herb",
    searchable_by=["Life Herb", "Item"],
    subtypes=["Item"],
    collector_number=90,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
