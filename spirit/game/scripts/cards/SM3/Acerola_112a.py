"""STUB: effect not implemented — do not guess mechanics.
Acerola (SM3 #112a): trainer effect stubbed.

Card text:
  - Put 1 of your Pokémon that has any damage counters on it and all cards attached to it into your hand.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="14a0b888-bb49-5ec2-82c4-42948c835eb5",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Acerola.Name",
    display_name="Acerola",
    searchable_by=["Acerola", "Supporter"],
    subtypes=["Supporter"],
    collector_number=175,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
