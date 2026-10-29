"""STUB: effect not implemented — do not guess mechanics.
Poké Ball (EX1 #86): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, search your deck for a Basic Pokémon or Evolution card, show it to your opponent and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e1e5dd66-c185-5c10-86f7-0ee7597858fd",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
