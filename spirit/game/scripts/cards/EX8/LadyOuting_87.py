"""STUB: effect not implemented — do not guess mechanics.
Lady Outing (EX8 #87): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your deck for up to 3 different types of basic Energy cards, show them to your opponent, and put them into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="36d1a2b0-3ffe-5c76-8c00-213f72554996",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LadyOuting.Name",
    display_name="Lady Outing",
    searchable_by=["Lady Outing", "Supporter"],
    subtypes=["Supporter"],
    collector_number=87,
    set_code="EX8",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
