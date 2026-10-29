"""STUB: effect not implemented — do not guess mechanics.
Lt. Surge's Strategy (HF #60): trainer effect stubbed.

Card text:
  - You can play this card only if you have more Prize cards remaining than your opponent.
  - During this turn, you can play 3 Supporter cards (including this card).
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="29225ded-583d-5cec-a0c4-0a048aa5a8a0",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LtSurgesStrategy.Name",
    display_name="Lt. Surge's Strategy",
    searchable_by=["Lt. Surge's Strategy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=60,
    set_code="HF",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
