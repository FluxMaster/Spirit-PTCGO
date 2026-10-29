"""STUB: effect not implemented — do not guess mechanics.
Fisherman (SM7 #130): trainer effect stubbed.

Card text:
  - Put 4 basic Energy cards from your discard pile into your hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="6c648258-1058-5488-b953-fe35b56cd1be",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fisherman.Name",
    display_name="Fisherman",
    searchable_by=["Fisherman", "Supporter"],
    subtypes=["Supporter"],
    collector_number=130,
    set_code="SM7",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
