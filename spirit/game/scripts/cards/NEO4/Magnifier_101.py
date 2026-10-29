"""STUB: effect not implemented — do not guess mechanics.
Magnifier (NEO4 #101): trainer effect stubbed.

Card text:
  - Attach Magnifier to 1 of your Pokémon. At the end of your turn, discard Magnifier. If the Pokémon Magnifier is attached to attacks, don't apply Resistance for that attack.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="8e7c9327-face-5c1f-9331-1083aa0b9a10",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Magnifier.Name",
    display_name="Magnifier",
    searchable_by=["Magnifier"],
    subtypes=[],
    collector_number=101,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
