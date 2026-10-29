"""STUB: effect not implemented — do not guess mechanics.
PokéGear (NEO1 #88): trainer effect stubbed.

Card text:
  - Look at the top 7 cards of your deck. If any of them are Trainer cards, you may show 1 of them to your opponent and put it into your hand. Shuffle your deck afterward. You can't play any more Trainer cards this turn.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="5bb6a32e-1e6e-5218-ac5d-0979cf370797",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PokeGear.Name",
    display_name="PokéGear",
    searchable_by=["Pok\u00e9Gear"],
    subtypes=[],
    collector_number=88,
    set_code="NEO1",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
