"""STUB: effect not implemented — do not guess mechanics.
Gust of Wind (BASE1 #93): trainer effect stubbed.

Card text:
  - Choose 1 of your opponent's Benched Pokémon and switch it with his or her Active Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="972d7ee6-3386-5e82-b6c8-6c82034aa920",
    key="BASE1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GustofWind.Name",
    display_name="Gust of Wind",
    searchable_by=["Gust of Wind"],
    subtypes=[],
    collector_number=93,
    set_code="BASE1",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
