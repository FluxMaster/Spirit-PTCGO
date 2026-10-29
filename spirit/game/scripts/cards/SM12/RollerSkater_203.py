"""STUB: effect not implemented — do not guess mechanics.
Roller Skater (SM12 #203): trainer effect stubbed.

Card text:
  - Discard a card from your hand. If you do, draw 2 cards. If you discarded an Energy card in this way, draw 2 more cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="a21675b6-9b09-5d9d-b191-183260ce7063",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.RollerSkater.Name",
    display_name="Roller Skater",
    searchable_by=["Roller Skater", "Supporter"],
    subtypes=["Supporter"],
    collector_number=203,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
