"""STUB: effect not implemented — do not guess mechanics.
Bill's Maintenance (ECARD1 #137): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - If you have any cards in your hand, shuffle 1 of them into your deck, then draw 3 cards.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="004561a8-5f5d-50ed-bcca-f77946f3b105",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BillsMaintenance.Name",
    display_name="Bill's Maintenance",
    searchable_by=["Bill's Maintenance", "Supporter"],
    subtypes=["Supporter"],
    collector_number=137,
    set_code="ECARD1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
