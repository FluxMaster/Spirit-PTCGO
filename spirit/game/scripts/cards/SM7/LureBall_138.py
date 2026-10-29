"""STUB: effect not implemented — do not guess mechanics.
Lure Ball (SM7 #138): trainer effect stubbed.

Card text:
  - Flip 3 coins. For each heads, put an Evolution Pokémon from your discard pile into your hand.
  - You may play as many Item cards as you like during your turn (before your attack).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="ae5aff8d-6e25-5337-be44-b61d399090c0",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LureBall.Name",
    display_name="Lure Ball",
    searchable_by=["Lure Ball", "Item"],
    subtypes=["Item"],
    collector_number=138,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
