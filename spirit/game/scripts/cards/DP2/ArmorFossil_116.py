"""STUB: effect not implemented — do not guess mechanics.
Armor Fossil (DP2 #116): trainer effect stubbed.

Card text:
  - Play Armor Fossil as if it were a Colorless Basic Pokémon. (Armor Fossil counts as a Trainer card as well, but if Armor Fossil is Knocked Out, this counts as a Knocked Out Pokémon.) Armor Fossil can't be affected by any Special Conditions and can't retreat. At any time during your turn before your attack, you may discard Armor Fossil from play. (This doesn't count as a Knocked Out Pokémon.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="387c8fab-9c97-57f4-b557-3690609b8461",
    key="DP2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ArmorFossil.Name",
    display_name="Armor Fossil",
    searchable_by=["Armor Fossil", "Item"],
    subtypes=["Item"],
    collector_number=116,
    set_code="DP2",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
