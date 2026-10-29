"""STUB: effect not implemented — do not guess mechanics.
Bill's Maintenance (SM7 #162): trainer effect stubbed.

Card text:
  - Shuffle a card from your hand into your deck. If you do, draw 3 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="7d12bfa5-bb81-5ef2-a381-10b96cf6afeb",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsMaintenance.Name",
    display_name="Bill's Maintenance",
    searchable_by=["Bill's Maintenance", "Supporter"],
    subtypes=["Supporter"],
    collector_number=162,
    set_code="SM7",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
