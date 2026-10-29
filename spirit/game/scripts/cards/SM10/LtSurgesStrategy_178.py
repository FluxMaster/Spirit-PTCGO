"""STUB: effect not implemented — do not guess mechanics.
Lt. Surge's Strategy (SM10 #178): trainer effect stubbed.

Card text:
  - You can play this card only if you have more Prize cards remaining than your opponent.
  - During this turn, you can play 3 Supporter cards (including this card).
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="4adcd302-f528-5c6e-afe4-653e842e3ee5",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LtSurgesStrategy.Name",
    display_name="Lt. Surge's Strategy",
    searchable_by=["Lt. Surge's Strategy", "Supporter"],
    subtypes=["Supporter"],
    collector_number=178,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
