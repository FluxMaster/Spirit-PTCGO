"""STUB: effect not implemented — do not guess mechanics.
Janine (SM10 #210): trainer effect stubbed.

Card text:
  - Look at the top 4 cards of your deck and put 2 of them into your hand. Shuffle the other cards back into your deck.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="05f5918c-1289-521e-88d2-2d83ec6486ad",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Janine.Name",
    display_name="Janine",
    searchable_by=["Janine", "Supporter"],
    subtypes=["Supporter"],
    collector_number=210,
    set_code="SM10",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
