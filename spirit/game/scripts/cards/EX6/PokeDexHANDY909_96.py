"""STUB: effect not implemented — do not guess mechanics.
PokéDex HANDY909 (EX6 #96): trainer effect stubbed.

Card text:
  - Shuffle your deck. Look at 6 cards from the top of your deck, then put them back on top of your deck in any order.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="f7a7239d-41b0-513e-9374-b71d9d71612e",
    key="EX6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeDexHANDY909.Name",
    display_name="PokéDex HANDY909",
    searchable_by=["Pok\u00e9Dex HANDY909", "Item"],
    subtypes=["Item"],
    collector_number=96,
    set_code="EX6",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
