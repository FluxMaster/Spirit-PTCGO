"""STUB: effect not implemented — do not guess mechanics.
Mysterious Fossil (EX12 #79): trainer effect stubbed.

Card text:
  - Play Mysterious Fossil as if it were a Basic Pokémon. While in play, Mysterious Fossil counts as a Colorless Pokémon (as well as a Trainer card). Mysterious Fossil has no attacks of its own, can't retreat, and can't be affected by any Special Conditions. If Mysterious Fossil is Knocked Out, it doesn't count as a Knocked Out Pokémon. (Discard it anyway.) At any time during your turn before your attack, you may discard Mysterious Fossil from play.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="2af02f87-56c8-53fe-9489-e2f7aee433cf",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousFossil.Name",
    display_name="Mysterious Fossil",
    searchable_by=["Mysterious Fossil", "Item"],
    subtypes=["Item"],
    collector_number=79,
    set_code="EX12",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
