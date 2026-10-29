"""STUB: effect not implemented — do not guess mechanics.
Lady (HF #SV86): trainer effect stubbed.

Card text:
  - Search your deck for up to 4 basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="9d694724-7791-5d1c-8ce0-343194d7b910",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Lady.Name",
    display_name="Lady",
    searchable_by=["Lady", "Supporter"],
    subtypes=["Supporter"],
    collector_number=155,
    set_code="HF",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
