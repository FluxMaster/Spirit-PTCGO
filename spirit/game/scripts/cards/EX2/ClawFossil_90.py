"""STUB: effect not implemented — do not guess mechanics.
Claw Fossil (EX2 #90): trainer effect stubbed.

Card text:
  - Play Claw Fossil as if it were a Basic Pokémon. While in play, Claw Fossil counts as a Colorless Pokémon (instead of a Trainer card). Claw Fossil has no attacks of its own, can't retreat, and can't be affected by any Special Conditions. If Claw Fossil is Knocked Out, it doesn't count as a Knocked Out Pokémon. (Discard it anyway.) At any time during your turn before your attack, you may discard Claw Fossil from play.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="0fcc4201-fd64-5463-9252-830e41030419",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ClawFossil.Name",
    display_name="Claw Fossil",
    searchable_by=["Claw Fossil", "Item"],
    subtypes=["Item"],
    collector_number=90,
    set_code="EX2",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
