"""STUB: effect not implemented — do not guess mechanics.
Copycat (SM7 #163): trainer effect stubbed.

Card text:
  - Shuffle your hand into your deck. Then, draw a card for each card in your opponent's hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="d256b5ed-7e16-582d-9828-0e8f68580918",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Copycat.Name",
    display_name="Copycat",
    searchable_by=["Copycat", "Supporter"],
    subtypes=["Supporter"],
    collector_number=163,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
