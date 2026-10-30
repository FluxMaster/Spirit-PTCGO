"""STUB: effect not implemented — do not guess mechanics.
Holon Scientist (EX11 #97): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Discard a card from your hand. If you can't discard a card from your hand, you can't play this card.
  - If you have less cards in your hand than your opponent, draw cards until you have the same number of cards as your opponent.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="195a4523-8cb3-5d4f-94fa-3f77d04ac369",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonScientist.Name",
    display_name="Holon Scientist",
    searchable_by=["Holon Scientist", "Supporter"],
    subtypes=["Supporter"],
    collector_number=97,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
