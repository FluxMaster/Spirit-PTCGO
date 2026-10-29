"""STUB: effect not implemented — do not guess mechanics.
New Pokédex (NEO1 #95): trainer effect stubbed.

Card text:
  - Shuffle your deck. Then, look at up to 5 cards from the top of your deck and rearrange them as you like.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="a6380331-b72d-51d8-9539-ff06e088b34a",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.NewPokedex.Name",
    display_name="New Pokédex",
    searchable_by=["New Pok\u00e9dex"],
    subtypes=[],
    collector_number=95,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
