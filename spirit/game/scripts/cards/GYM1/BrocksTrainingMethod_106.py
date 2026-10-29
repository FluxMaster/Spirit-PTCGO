"""STUB: effect not implemented — do not guess mechanics.
Brock's Training Method (GYM1 #106): trainer effect stubbed.

Card text:
  - Search your deck for a Basic Pokémon or Evolution card with Brock in its name. Show that card to your opponent, then put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="366c7650-ebff-5de4-b32b-80a20bd0600a",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksTrainingMethod.Name",
    display_name="Brock's Training Method",
    searchable_by=["Brock's Training Method"],
    subtypes=[],
    collector_number=106,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
