"""STUB: effect not implemented — do not guess mechanics.
Energy Amplifier (NEO4 #98): trainer effect stubbed.

Card text:
  - Choose an Energy card in your hand, show it to your opponent, and shuffle it into your deck. Then flip a coin. If heads, search your deck for up to 3 basic Energy cards. Show them to your opponent, and put them into your hand. Shuffle your deck afterward.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="a88e1551-714b-5896-9da4-eeecb122d0c4",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.trainer.EnergyAmplifier.Name",
    display_name="Energy Amplifier",
    searchable_by=["Energy Amplifier"],
    subtypes=[],
    collector_number=98,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
