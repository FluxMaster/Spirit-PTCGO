"""STUB: effect not implemented — do not guess mechanics.
Giovanni (GYM2 #18): trainer effect stubbed.

Card text:
  - Choose 1 of your Pokémon in play with Giovanni in its name. For the rest of your turn, you may evolve that Pokémon even if you just played or evolved it this turn or if this is your first turn. This effect also applies to the Pokémon it evolves into.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="43919234-6fbb-5ffa-b663-001b09ab8cd4",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Giovanni.Name",
    display_name="Giovanni",
    searchable_by=["Giovanni"],
    subtypes=[],
    collector_number=18,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
