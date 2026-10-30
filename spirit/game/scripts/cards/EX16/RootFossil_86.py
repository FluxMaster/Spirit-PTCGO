"""STUB: effect not implemented — do not guess mechanics.
Root Fossil (EX16 #86): trainer effect stubbed.

Card text:
  - Play Root Fossil as if it were a Basic Pokémon. While in play, Root Fossil counts as a Colorless Pokémon (as well as a Trainer card). Root Fossil has no attacks of its own, can't retreat, and can't be affected by any Special Conditions. If Root Fossil is Knocked Out, it doesn't count as a Knocked Out Pokémon. (Discard it anyway.) At any time during your turn before your attack, you may discard Root Fossil from play.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="bc983b4d-41d8-5512-9ca8-4ee390bf89c0",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RootFossil.Name",
    display_name="Root Fossil",
    searchable_by=["Root Fossil", "Item"],
    subtypes=["Item"],
    collector_number=86,
    set_code="EX16",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
