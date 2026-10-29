"""STUB: effect not implemented — do not guess mechanics.
PlusPower (BASE1 #84): trainer effect stubbed.

Card text:
  - Attach PlusPower to your Active Pokémon. At the end of your turn, discard PlusPower. If this Pokémon's attack does damage to the Defending Pokémon (after applying Weakness and Resistance), the attack does 10 more damage to the Defending Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="48e34518-e255-5c0b-8a5e-88139b2db800",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PlusPower.Name",
    display_name="PlusPower",
    searchable_by=["PlusPower"],
    subtypes=[],
    collector_number=84,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
