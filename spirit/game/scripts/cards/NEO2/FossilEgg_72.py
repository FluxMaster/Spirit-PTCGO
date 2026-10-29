"""STUB: effect not implemented — do not guess mechanics.
Fossil Egg (NEO2 #72): trainer effect stubbed.

Card text:
  - Flip a coin. If heads, search your deck for a card that evolves from Mysterious Fossil and put it onto your Bench or put a card that evolves from Mysterious Fossil from your hand onto your Bench. Either way, treat the new card as a Basic Pokémon. If you searched your deck, shuffle it. (You can't play this card if your Bench is full.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="8705713e-33f5-5de5-87af-5a3304666223",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FossilEgg.Name",
    display_name="Fossil Egg",
    searchable_by=["Fossil Egg"],
    subtypes=[],
    collector_number=72,
    set_code="NEO2",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
