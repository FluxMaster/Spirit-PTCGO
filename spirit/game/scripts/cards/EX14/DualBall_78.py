"""STUB: effect not implemented — do not guess mechanics.
Dual Ball (EX14 #78): trainer effect stubbed.

Card text:
  - Flip 2 coins. For each heads, search your deck for a Basic Pokémon card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="acabb243-f3f0-555a-adfa-68dda60907c8",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DualBall.Name",
    display_name="Dual Ball",
    searchable_by=["Dual Ball", "Item"],
    subtypes=["Item"],
    collector_number=78,
    set_code="EX14",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
