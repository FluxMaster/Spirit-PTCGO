"""STUB: effect not implemented — do not guess mechanics.
Gust of Wind (BASE4 #120): trainer effect stubbed.

Card text:
  - Choose 1 of your opponent's Benched Pokémon and switch it with his or her Active Pokémon.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="beed2548-4563-5060-8181-6326bcd7aea0",
    key="BASE4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.GustofWind.Name",
    display_name="Gust of Wind",
    searchable_by=["Gust of Wind"],
    subtypes=[],
    collector_number=120,
    set_code="BASE4",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
