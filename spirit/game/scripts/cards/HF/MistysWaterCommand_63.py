"""STUB: effect not implemented — do not guess mechanics.
Misty's Water Command (HF #63): trainer effect stubbed.

Card text:
  - Move any number of Water Energy from your Pokémon to your Psyduck, Horsea, Staryu, Starmie-GX, Magikarp, Gyarados, or Lapras in any way you like.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="5ee0e1b4-cc2f-5626-9bb6-4548f3ba703d",
    key="HF",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MistysWaterCommand.Name",
    display_name="Misty's Water Command",
    searchable_by=["Misty's Water Command", "Supporter"],
    subtypes=["Supporter"],
    collector_number=63,
    set_code="HF",
    rarity=Rarities.RareHolo,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
