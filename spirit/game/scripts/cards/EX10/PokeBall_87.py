"""STUB: effect not implemented — do not guess mechanics.
Poké Ball (EX10 #87): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, search your deck for a Basic Pokémon or Evolution card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="fbadefb7-7013-5032-a300-5e5615b039fe",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeBall.Name",
    display_name="Poké Ball",
    searchable_by=["Pok\u00e9 Ball", "Item"],
    subtypes=["Item"],
    collector_number=87,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
