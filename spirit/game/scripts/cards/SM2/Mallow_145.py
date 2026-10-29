"""STUB: effect not implemented — do not guess mechanics.
Mallow (SM2 #145): trainer effect stubbed.

Card text:
  - Search your deck for 2 cards, shuffle your deck, then put those cards on top of it in any order.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="8950d6b8-765a-59c0-91b7-e44b5cc149b3",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Mallow.Name",
    display_name="Mallow",
    searchable_by=["Mallow", "Supporter"],
    subtypes=["Supporter"],
    collector_number=145,
    set_code="SM2",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
