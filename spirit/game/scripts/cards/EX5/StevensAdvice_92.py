"""STUB: effect not implemented — do not guess mechanics.
Steven's Advice (EX5 #92): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Draw a number of cards up to the number of your opponent's Pokémon in play.
  - If you have more than 7 cards (including this one) in your hand, you can't play this card.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="25e2b4fb-8b58-5b04-a194-09894b6545c3",
    key="EX5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StevensAdvice.Name",
    display_name="Steven's Advice",
    searchable_by=["Steven's Advice", "Supporter"],
    subtypes=["Supporter"],
    collector_number=92,
    set_code="EX5",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
