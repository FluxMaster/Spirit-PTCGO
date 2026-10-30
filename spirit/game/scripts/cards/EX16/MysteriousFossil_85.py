"""STUB: effect not implemented — do not guess mechanics.
Mysterious Fossil (EX16 #85): trainer effect stubbed.

Card text:
  - Play Mysterious Fossil as if it were a Basic Pokémon. While in play, Mysterious Fossil counts as a Colorless Pokémon (as well as a Trainer card). Mysterious Fossil has no attacks of its own, can't retreat, and can't be affected by any Special Conditions. If Mysterious Fossil is Knocked Out, it doesn't count as a Knocked Out Pokémon. (Discard it anyway.) At any time during your turn before your attack, you may discard Mysterious Fossil from play.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="099c29e6-93bb-5b05-b70d-e54ba6f5edfb",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MysteriousFossil.Name",
    display_name="Mysterious Fossil",
    searchable_by=["Mysterious Fossil", "Item"],
    subtypes=["Item"],
    collector_number=85,
    set_code="EX16",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
