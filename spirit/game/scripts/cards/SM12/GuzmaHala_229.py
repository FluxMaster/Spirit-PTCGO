"""STUB: effect not implemented — do not guess mechanics.
Guzma & Hala (SM12 #229): trainer effect stubbed.

Card text:
  - Search your deck for a Stadium card, reveal it, and put it into your hand. Then, shuffle your deck.
  - When you play this card, you may discard 2 other cards from your hand. If you do, you may also search for a Pokémon Tool card and a Special Energy card in this way.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="0cc365dd-1358-59a7-9898-886d34efdcd8",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GuzmaHala.Name",
    display_name="Guzma & Hala",
    searchable_by=["Guzma & Hala", "Supporter", "TAG TEAM"],
    subtypes=["Supporter", "TAG TEAM"],
    collector_number=229,
    set_code="SM12",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
