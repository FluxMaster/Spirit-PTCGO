"""STUB: effect not implemented — do not guess mechanics.
Fieldworker (EX12 #73): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Draw 3 cards. Your opponent may also draw a card.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="1b5a5348-83e6-52c5-ac7a-e31ba5e339a1",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fieldworker.Name",
    display_name="Fieldworker",
    searchable_by=["Fieldworker", "Supporter"],
    subtypes=["Supporter"],
    collector_number=73,
    set_code="EX12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
