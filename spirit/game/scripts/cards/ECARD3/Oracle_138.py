"""STUB: effect not implemented — do not guess mechanics.
Oracle (ECARD3 #138): trainer effect stubbed.

Card text:
  - You can play only 1 Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Choose 2 cards from your deck and shuffle the rest of your deck. Put the chosen cards on top of your deck in any order.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="3358863d-bf4d-575d-b784-04f0754a6116",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Oracle.Name",
    display_name="Oracle",
    searchable_by=["Oracle", "Supporter"],
    subtypes=["Supporter"],
    collector_number=138,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
