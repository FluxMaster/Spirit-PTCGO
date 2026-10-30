"""STUB: effect not implemented — do not guess mechanics.
Root Fossil (EX12 #80): trainer effect stubbed.

Card text:
  - Play Root Fossil as if it were a Basic Pokémon. While in play, Root Fossil counts as a Colorless Pokémon (as well as a Trainer card). Root Fossil has no attacks of its own, can't retreat, and can't be affected by any Special Conditions. If Root Fossil is Knocked Out, it doesn't count as a Knocked Out Pokémon. (Discard it anyway.) At any time during your turn before your attack, you may discard Root Fossil from play.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="eb644d15-542d-5835-9d7b-785f7a822e9e",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RootFossil.Name",
    display_name="Root Fossil",
    searchable_by=["Root Fossil", "Item"],
    subtypes=["Item"],
    collector_number=80,
    set_code="EX12",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
