"""STUB: effect not implemented — do not guess mechanics.
Professor Elm (BP #3): trainer effect stubbed.

Card text:
  - Shuffle your hand into your deck. Then, draw 7 cards. You can't play any more Trainer cards this turn.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="706feb4c-fadd-509d-9b08-72219cc312ed",
    key="BP",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorElm.Name",
    display_name="Professor Elm",
    searchable_by=["Professor Elm"],
    subtypes=[],
    collector_number=3,
    set_code="BP",
    rarity=Rarities.RarePromo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
