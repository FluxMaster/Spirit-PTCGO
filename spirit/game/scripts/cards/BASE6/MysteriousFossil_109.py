"""STUB: effect not implemented — do not guess mechanics.
Mysterious Fossil (BASE6 #109): trainer effect stubbed.

Card text:
  - Play Mysterious Fossil as if it were a Basic Pokémon. While in play, Mysterious Fossil counts as a Pokémon (instead of a Trainer card). Mysterious Fossil has no attacks, can't retreat, and can't be affected by Special Conditions. If Mysterious Fossil is Knocked Out, it doesn't count as a Knocked Out Pokémon. (Discard it anyway.) At any time during your turn before your attack, you may discard Mysterious Fossil from play. You can put Pokémon that evolve from Mysterious Fossil on this card.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="18b2ea39-96c8-5eae-85c0-d4aacd06c58b",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousFossil.Name",
    display_name="Mysterious Fossil",
    searchable_by=["Mysterious Fossil"],
    subtypes=[],
    collector_number=109,
    set_code="BASE6",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
