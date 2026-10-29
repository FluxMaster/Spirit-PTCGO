"""STUB: effect not implemented — do not guess mechanics.
Evelyn (SM9 #175): trainer effect stubbed.

Card text:
  - You can play this card only if your opponent's Active Pokémon is a Stage 1 Pokémon.
  - Draw 4 cards.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="2cf723f0-d7bc-5cee-81b0-216b65c1bbcd",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Evelyn.Name",
    display_name="Evelyn",
    searchable_by=["Evelyn", "Supporter"],
    subtypes=["Supporter"],
    collector_number=175,
    set_code="SM9",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
