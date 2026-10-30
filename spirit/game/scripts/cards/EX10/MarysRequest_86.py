"""STUB: effect not implemented — do not guess mechanics.
Mary's Request (EX10 #86): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Draw a card. If you don't have any Stage 2 Evolved Pokémon in play, draw 2 more cards.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="7aa632dd-492d-5b8d-ad8b-c79660e635cb",
    key="EX10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MarysRequest.Name",
    display_name="Mary's Request",
    searchable_by=["Mary's Request", "Supporter"],
    subtypes=["Supporter"],
    collector_number=86,
    set_code="EX10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
