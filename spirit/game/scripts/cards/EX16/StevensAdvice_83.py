"""STUB: effect not implemented — do not guess mechanics.
Steven's Advice (EX16 #83): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Draw a number of cards up to the number of your opponent's Pokémon in play.
  - If you have 7 or more cards (including this one) in your hand, you can't play this card.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="74016157-7106-526d-aaef-a70b0f76b93d",
    key="EX16",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StevensAdvice.Name",
    display_name="Steven's Advice",
    searchable_by=["Steven's Advice", "Supporter"],
    subtypes=["Supporter"],
    collector_number=83,
    set_code="EX16",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
