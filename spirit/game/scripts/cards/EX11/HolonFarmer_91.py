"""STUB: effect not implemented — do not guess mechanics.
Holon Farmer (EX11 #91): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Discard a card from your hand. If you can't discard a card from your hand, you can't play this card.
  - Search your discard pile for 3 basic Energy cards and any combination of 3 Basic Pokémon or Evolution cards, show them to your opponent, and put them on top of your deck. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="38f2715f-12ae-5e96-9eb4-6ec4a2aa8e65",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonFarmer.Name",
    display_name="Holon Farmer",
    searchable_by=["Holon Farmer", "Supporter"],
    subtypes=["Supporter"],
    collector_number=91,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
