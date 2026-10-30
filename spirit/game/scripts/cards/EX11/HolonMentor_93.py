"""STUB: effect not implemented — do not guess mechanics.
Holon Mentor (EX11 #93): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Discard a card from your hand. If you can't discard a card from your hand, you can't play this card.
  - Search your deck for up to 3 Basic Pokémon that each has 100 HP or less, show them to your opponent, and put them into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="96273697-7dfc-56d8-b71f-92b917da80cb",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonMentor.Name",
    display_name="Holon Mentor",
    searchable_by=["Holon Mentor", "Supporter"],
    subtypes=["Supporter"],
    collector_number=93,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
