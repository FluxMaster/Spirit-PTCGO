"""STUB: effect not implemented — do not guess mechanics.
Channeler (SM11 #232): trainer effect stubbed.

Card text:
  - Remove all effects of attacks on you and each of your Pokémon.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="809692a1-a00e-5176-8900-c143eeca9d37",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Channeler.Name",
    display_name="Channeler",
    searchable_by=["Channeler", "Supporter"],
    subtypes=["Supporter"],
    collector_number=232,
    set_code="SM11",
    rarity=Rarities.RareUltra,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
