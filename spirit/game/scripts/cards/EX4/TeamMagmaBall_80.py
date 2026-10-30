"""STUB: effect not implemented — do not guess mechanics.
Team Magma Ball (EX4 #80): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, search your deck for a Pokémon that has Team Magma in its name, show it to your opponent, and put it into your hand. If tails, search your deck for a Basic Pokémon that has Team Magma in its name, show it to your opponent and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="918dc69a-2573-5528-a2c9-c892c386e373",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.TeamMagmaBall.Name",
    display_name="Team Magma Ball",
    searchable_by=["Team Magma Ball", "Item"],
    subtypes=["Item"],
    collector_number=80,
    set_code="EX4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
