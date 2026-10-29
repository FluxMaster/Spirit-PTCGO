"""STUB: effect not implemented — do not guess mechanics.
Brock (GYM1 #98): trainer effect stubbed.

Card text:
  - Remove 1 damage counter from each of your Pokémon that has any damage counters on it.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="08202675-968e-51ca-a73b-ed173c4f300d",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Brock.Name",
    display_name="Brock",
    searchable_by=["Brock"],
    subtypes=[],
    collector_number=98,
    set_code="GYM1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
