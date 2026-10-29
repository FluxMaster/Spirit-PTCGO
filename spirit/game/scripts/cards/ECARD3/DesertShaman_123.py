"""STUB: effect not implemented — do not guess mechanics.
Desert Shaman (ECARD3 #123): trainer effect stubbed.

Card text:
  - You can play only 1 Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Shuffle your hand into your deck and draw up to 4 cards. Your opponent does the same.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="56a14c5e-dbbf-5d20-b874-4bba005c042b",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.DesertShaman.Name",
    display_name="Desert Shaman",
    searchable_by=["Desert Shaman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=123,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
