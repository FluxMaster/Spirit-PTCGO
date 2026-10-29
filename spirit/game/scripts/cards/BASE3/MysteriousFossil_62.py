"""STUB: effect not implemented — do not guess mechanics.
Mysterious Fossil (BASE3 #62): trainer effect stubbed.

Card text:
  - Play Mysterious Fossil as if it were a Basic Pokémon. While in play, Mysterious Fossil counts as a Pokémon (instead of a Trainer card). Mysterious Fossil has no attacks, can't retreat, and can't be Asleep, Confused, Paralyzed, or Poisoned. If Mysterious Fossil is Knocked Out, it doesn't count as a Knocked Out Pokémon. (Discard it anyway.) At any time during your turn before your attack, you may discard Mysterious Fossil from play.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="9ec980d4-54cf-533d-8c98-426aa73fff4c",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousFossil.Name",
    display_name="Mysterious Fossil",
    searchable_by=["Mysterious Fossil"],
    subtypes=[],
    collector_number=62,
    set_code="BASE3",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
