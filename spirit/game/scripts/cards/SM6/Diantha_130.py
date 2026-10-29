"""STUB: effect not implemented — do not guess mechanics.
Diantha (SM6 #130): trainer effect stubbed.

Card text:
  - You can play this card only if 1 of your Fairy Pokémon was Knocked Out during your opponent's last turn.
  - Put 2 cards from your discard pile into your hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="357fcd88-9c1a-55d4-8a62-6c00a8960d33",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Diantha.Name",
    display_name="Diantha",
    searchable_by=["Diantha", "Supporter"],
    subtypes=["Supporter"],
    collector_number=130,
    set_code="SM6",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
