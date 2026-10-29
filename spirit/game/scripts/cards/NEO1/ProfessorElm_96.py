"""STUB: effect not implemented — do not guess mechanics.
Professor Elm (NEO1 #96): trainer effect stubbed.

Card text:
  - Shuffle your hand into your deck. Then, draw 7 cards. You can't play any more Trainer cards this turn.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="270bdfe3-71b0-5f30-b9eb-90f6792edff9",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorElm.Name",
    display_name="Professor Elm",
    searchable_by=["Professor Elm"],
    subtypes=[],
    collector_number=96,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
