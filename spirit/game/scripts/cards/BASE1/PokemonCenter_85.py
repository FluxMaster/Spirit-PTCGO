"""STUB: effect not implemented — do not guess mechanics.
Pokémon Center (BASE1 #85): trainer effect stubbed.

Card text:
  - Remove all damage counters from all of your own Pokémon with damage counters on them, then discard all Energy cards attached to those Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e9728209-ae39-5204-ae97-b70869663e0e",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonCenter.Name",
    display_name="Pokémon Center",
    searchable_by=["Pok\u00e9mon Center"],
    subtypes=[],
    collector_number=85,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
