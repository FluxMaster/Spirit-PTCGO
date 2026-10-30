"""STUB: effect not implemented — do not guess mechanics.
Skull Fossil (DP2 #117): trainer effect stubbed.

Card text:
  - Play Skull Fossil as if it were a Colorless Basic Pokémon. (Skull Fossil counts as a Trainer card as well, but if Skull Fossil is Knocked Out, this counts as a Knocked Out Pokémon.) Skull Fossil can't be affected by any Special Conditions and can't retreat. At any time during your turn before your attack, you may discard Skull Fossil from play. (This doesn't count as a Knocked Out Pokémon.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="976c54d0-e02d-5f4d-84a9-e20a6e2dba23",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SkullFossil.Name",
    display_name="Skull Fossil",
    searchable_by=["Skull Fossil", "Item"],
    subtypes=["Item"],
    collector_number=117,
    set_code="DP2",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
