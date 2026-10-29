"""STUB: effect not implemented — do not guess mechanics.
Diantha (SM6 #105): trainer effect stubbed.

Card text:
  - You can play this card only if 1 of your Fairy Pokémon was Knocked Out during your opponent's last turn.
  - Put 2 cards from your discard pile into your hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="3cc15279-2c3e-50aa-960c-1fc236e33ca7",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Diantha.Name",
    display_name="Diantha",
    searchable_by=["Diantha", "Supporter"],
    subtypes=["Supporter"],
    collector_number=105,
    set_code="SM6",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
