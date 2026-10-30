"""STUB: effect not implemented — do not guess mechanics.
Holon Researcher (EX11 #95): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Discard a card from your hand. If you can't discard a card from your hand, you can't play this card.
  - Search your deck for a Metal Energy card or a Basic Pokémon (or Evolution card) that has δ on its card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="735f78ef-f7c2-523e-a612-92b4ffe40595",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonResearcher.Name",
    display_name="Holon Researcher",
    searchable_by=["Holon Researcher", "Supporter"],
    subtypes=["Supporter"],
    collector_number=95,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
