"""STUB: effect not implemented — do not guess mechanics.
Jessie & James (HF #68): trainer effect stubbed.

Card text:
  - Each player discards 2 cards from their hand. Your opponent discards first.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="4c177700-8b69-5360-9e46-21af47b77315",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JessieJames.Name",
    display_name="Jessie & James",
    searchable_by=["Jessie & James", "Supporter"],
    subtypes=["Supporter"],
    collector_number=68,
    set_code="HF",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
