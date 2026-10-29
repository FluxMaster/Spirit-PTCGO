"""STUB: effect not implemented — do not guess mechanics.
Mysterious Fossil (EX2 #91): trainer effect stubbed.

Card text:
  - Play Mysterious Fossil as if it were a Basic Pokémon. While in play, Mysterious Fossil counts as a Colorless Pokémon (instead of a Trainer card). Mysterious Fossil has no attacks of its own, can't retreat, and can't be affected by any Special Conditions. If Mysterious is Knocked Out, it doesn't count as a Knocked Out Pokémon. (Discard it anyway.) At any time during your turn before your attack, you may discard Mysterious Fossil from play.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="342a3e62-e836-5b30-bf75-f44ce27ae012",
    key="EX2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousFossil.Name",
    display_name="Mysterious Fossil",
    searchable_by=["Mysterious Fossil", "Item"],
    subtypes=["Item"],
    collector_number=91,
    set_code="EX2",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
