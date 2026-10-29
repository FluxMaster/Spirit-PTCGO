"""STUB: effect not implemented — do not guess mechanics.
Bill's Maintenance (SM7 #126): trainer effect stubbed.

Card text:
  - Shuffle a card from your hand into your deck. If you do, draw 3 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="e00628fa-11fb-58c3-9b08-38955c6747ab",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsMaintenance.Name",
    display_name="Bill's Maintenance",
    searchable_by=["Bill's Maintenance", "Supporter"],
    subtypes=["Supporter"],
    collector_number=126,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
