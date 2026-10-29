"""STUB: effect not implemented — do not guess mechanics.
Revive (BASE1 #89): trainer effect stubbed.

Card text:
  - Put 1 Basic Pokémon card from your discard pile onto your Bench. Put damage counters on that Pokémon equal to half its HP (rounded down to the nearest 10). (You can't play Revive if your Bench is full.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b45cab76-43ab-53db-87d5-790f3ac63c9a",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Revive.Name",
    display_name="Revive",
    searchable_by=["Revive"],
    subtypes=[],
    collector_number=89,
    set_code="BASE1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
