"""STUB: effect not implemented — do not guess mechanics.
Kiawe (SM3 #116): trainer effect stubbed.

Card text:
  - Search your deck for up to 4 Fire Energy cards and attach them to 1 of your Pokémon. Then, shuffle your deck. Your turn ends.
  - You may play only 1 Supporter card during your turn (before your attack).
"""

from spirit.game.data_utils import SupporterCardDef, unimplemented
from spirit.game.attributes import Rarities

card = SupporterCardDef(
    guid="be3ca5ba-43d8-5792-9d4c-6d4ea7da4d07",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Kiawe.Name",
    display_name="Kiawe",
    searchable_by=["Kiawe", "Supporter"],
    subtypes=["Supporter"],
    collector_number=116,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
