"""STUB: effect not implemented — do not guess mechanics.
PlusPower (DP1 #109): trainer effect stubbed.

Card text:
  - Attach PlusPower to 1 of your Pokémon. Discard this card at the end of your turn.
  - If the Pokémon PlusPower is attached to attacks, the attack does 10 more damage to the Active Pokémon (before applying Weakness and Resistance).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="69fd2176-48c0-5434-a271-5c99e13b8ed6",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlusPower.Name",
    display_name="PlusPower",
    searchable_by=["PlusPower", "Item"],
    subtypes=["Item"],
    collector_number=109,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
