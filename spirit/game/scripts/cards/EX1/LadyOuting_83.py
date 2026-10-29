"""STUB: effect not implemented — do not guess mechanics.
Lady Outing (EX1 #83): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Search your deck for up to 3 different types of basic Energy cards, show them to your opponent, and put them into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="ac7f1d27-12a0-5915-9d35-381764d4a119",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LadyOuting.Name",
    display_name="Lady Outing",
    searchable_by=["Lady Outing", "Supporter"],
    subtypes=["Supporter"],
    collector_number=83,
    set_code="EX1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
