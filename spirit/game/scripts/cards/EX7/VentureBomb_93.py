"""STUB: effect not implemented — do not guess mechanics.
Venture Bomb (EX7 #93): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, put 1 damage counter on 1 of your opponent's Pokémon. If tails, put 1 damage counter on 1 of your Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="fda50f24-bb24-5446-95a7-f8f29acd2ea4",
    key="EX7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.VentureBomb.Name",
    display_name="Venture Bomb",
    searchable_by=["Venture Bomb", "Rocket's Secret Machine"],
    subtypes=["Rocket's Secret Machine"],
    collector_number=93,
    set_code="EX7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
