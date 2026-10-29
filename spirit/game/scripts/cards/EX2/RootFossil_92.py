"""STUB: effect not implemented — do not guess mechanics.
Root Fossil (EX2 #92): trainer effect stubbed.

Card text:
  - Play Root Fossil as if it were a Basic Pokémon. While in play, Root Fossil counts as a Colorless Pokémon (instead of a Trainer card). Root Fossil has no attacks of its own, can't retreat, and can't be affected by any Special Conditions. If Root Fossil is Knocked Out, it doesn't count as a Knocked Out Pokémon. (Discard it anyway.) At any time during your turn before your attack, you may discard Root Fossil from play.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="d461be57-f2a1-5b4a-9639-7493193bceb4",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RootFossil.Name",
    display_name="Root Fossil",
    searchable_by=["Root Fossil", "Item"],
    subtypes=["Item"],
    collector_number=92,
    set_code="EX2",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
