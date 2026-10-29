"""STUB: effect not implemented — do not guess mechanics.
Fisherman (HF #SV83): trainer effect stubbed.

Card text:
  - Put 4 basic Energy cards from your discard pile into your hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="1ed0d286-2d5e-55d5-a48d-3a5dab10626e",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fisherman.Name",
    display_name="Fisherman",
    searchable_by=["Fisherman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=152,
    set_code="HF",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
