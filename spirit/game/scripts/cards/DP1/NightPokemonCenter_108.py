"""STUB: effect not implemented — do not guess mechanics.
Night Pokémon Center (DP1 #108): trainer effect stubbed.

Card text:
  - Choose 1 of your Pokémon. Flip 2 coins. If both are heads, remove all damage counters from that Pokémon. If both are tails, discard all Energy cards attached to that Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="5b868f01-dfbf-55da-91d7-65bbc3face46",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NightPokemonCenter.Name",
    display_name="Night Pokémon Center",
    searchable_by=["Night Pok\u00e9mon Center", "Item"],
    subtypes=["Item"],
    collector_number=108,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
