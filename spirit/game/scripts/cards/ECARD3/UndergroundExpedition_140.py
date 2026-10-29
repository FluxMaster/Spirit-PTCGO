"""STUB: effect not implemented — do not guess mechanics.
Underground Expedition (ECARD3 #140): trainer effect stubbed.

Card text:
  - You can play only 1 Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Look at the bottom 4 cards of your deck. Put 2 of those cards into your hand, and then return the remaining cards to the bottom of your deck in any order.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="ea800af8-3660-55aa-afb1-8313ccd1e58a",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.UndergroundExpedition.Name",
    display_name="Underground Expedition",
    searchable_by=["Underground Expedition", "Supporter"],
    subtypes=["Supporter"],
    collector_number=140,
    set_code="ECARD3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
