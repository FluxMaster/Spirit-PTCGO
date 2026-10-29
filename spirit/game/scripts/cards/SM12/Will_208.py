"""STUB: effect not implemented — do not guess mechanics.
Will (SM12 #208): trainer effect stubbed.

Card text:
  - The next time you flip any number of coins for the effect of an attack, Ability, or Trainer card this turn, choose heads or tails for the first coin flip.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="768308fd-7a9c-54c9-b11f-6dc17f892fda",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Will.Name",
    display_name="Will",
    searchable_by=["Will", "Supporter"],
    subtypes=["Supporter"],
    collector_number=208,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
