"""STUB: effect not implemented — do not guess mechanics.
Rival (DP1 #113): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Reveal the top 5 cards of your deck. Your opponent chooses 3 of those cards. Put those cards into your hand and put other 2 cards on top of your deck. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="64b27ae8-3da3-5f08-a38e-c7995762fb40",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Rival.Name",
    display_name="Rival",
    searchable_by=["Rival", "Supporter"],
    subtypes=["Supporter"],
    collector_number=113,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
