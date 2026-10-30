"""STUB: effect not implemented — do not guess mechanics.
Claw Fossil (EX12 #78): trainer effect stubbed.

Card text:
  - Play Claw Fossil as if it were a Basic Pokémon. While in play, Claw Fossil counts as a Colorless Pokémon (as well as a Trainer card). Claw Fossil has no attacks of its own, can't retreat, and can't be affected by any Special Conditions. If Claw Fossil is Knocked Out, it doesn't count as a Knocked Out Pokémon. (Discard it anyway.) At any time during your turn before your attack, you may discard Claw Fossil from play.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="aee83d9e-a5bf-5997-afc9-1ce9e915d4f5",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ClawFossil.Name",
    display_name="Claw Fossil",
    searchable_by=["Claw Fossil", "Item"],
    subtypes=["Item"],
    collector_number=78,
    set_code="EX12",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
