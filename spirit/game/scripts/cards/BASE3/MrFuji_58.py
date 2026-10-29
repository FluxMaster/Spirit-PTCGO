"""STUB: effect not implemented — do not guess mechanics.
Mr. Fuji (BASE3 #58): trainer effect stubbed.

Card text:
  - Choose a Pokémon on your Bench. Shuffle it and any cards attached to it into your deck.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="adf5c669-018e-5a78-82f9-21f3013e9322",
    key="BASE3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MrFuji.Name",
    display_name="Mr. Fuji",
    searchable_by=["Mr. Fuji"],
    subtypes=[],
    collector_number=58,
    set_code="BASE3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
