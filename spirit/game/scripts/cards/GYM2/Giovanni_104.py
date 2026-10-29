"""STUB: effect not implemented — do not guess mechanics.
Giovanni (GYM2 #104): trainer effect stubbed.

Card text:
  - Choose 1 of your Pokémon in play with Giovanni in its name. For the rest of your turn, you may evolve that Pokémon even if you just played or evolved it this turn or if this is your first turn. This effect also applies to the Pokémon it evolves into.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="b06f16a8-994d-527a-81e4-751f8f38f907",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Giovanni.Name",
    display_name="Giovanni",
    searchable_by=["Giovanni"],
    subtypes=[],
    collector_number=104,
    set_code="GYM2",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
