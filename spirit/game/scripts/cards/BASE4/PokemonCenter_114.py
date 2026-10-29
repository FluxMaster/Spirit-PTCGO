"""STUB: effect not implemented — do not guess mechanics.
Pokémon Center (BASE4 #114): trainer effect stubbed.

Card text:
  - Remove all damage counters from all of your own Pokémon with damage counters on them, then discard all Energy cards attached to those Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e54f6176-665d-5446-bb35-ed5e01b0b3cd",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokemonCenter.Name",
    display_name="Pokémon Center",
    searchable_by=["Pok\u00e9mon Center"],
    subtypes=[],
    collector_number=114,
    set_code="BASE4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
