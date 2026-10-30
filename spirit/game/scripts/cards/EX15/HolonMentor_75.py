"""STUB: effect not implemented — do not guess mechanics.
Holon Mentor (EX15 #75): trainer effect stubbed.

Card text:
  - You can play only one Supporter card each turn. When you play this card, put it next to your Active Pokémon. When your turn ends, discard this card.
  - Discard a card from your hand. If you can't discard a card from your hand, you can't play this card.
  - Search your deck for up to 3 Basic Pokémon that each has 100 HP or less, show them to your opponent, and put them into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="56487d85-6838-5dbc-950b-643b06ce73c8",
    key="EX15",
    name="com.direwolfdigital.cake.data.archetypes.trainer.HolonMentor.Name",
    display_name="Holon Mentor",
    searchable_by=["Holon Mentor", "Supporter"],
    subtypes=["Supporter"],
    collector_number=75,
    set_code="EX15",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
