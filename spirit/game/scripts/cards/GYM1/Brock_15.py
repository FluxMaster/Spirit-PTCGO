"""STUB: effect not implemented — do not guess mechanics.
Brock (GYM1 #15): trainer effect stubbed.

Card text:
  - Remove 1 damage counter from each of your Pokémon that has any damage counters on it.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="af9cff4b-a4ad-533d-8618-170449b8f35e",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Brock.Name",
    display_name="Brock",
    searchable_by=["Brock"],
    subtypes=[],
    collector_number=15,
    set_code="GYM1",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
