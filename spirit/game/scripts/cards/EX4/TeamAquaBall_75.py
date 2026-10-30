"""STUB: effect not implemented — do not guess mechanics.
Team Aqua Ball (EX4 #75): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, search your deck for a Pokémon that has Team Aqua in its name, show it to your opponent, and put it into your hand. If tails, search your deck for a Basic Pokémon that has Team Aqua in its name, show it to your opponent and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="50e7f7f7-2dab-56b1-bd1a-aef5491f999a",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamAquaBall.Name",
    display_name="Team Aqua Ball",
    searchable_by=["Team Aqua Ball", "Item"],
    subtypes=["Item"],
    collector_number=75,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
