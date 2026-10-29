"""STUB: effect not implemented — do not guess mechanics.
Sabrina's ESP (GYM1 #117): trainer effect stubbed.

Card text:
  - Attach Sabrina's ESP to 1 of your Pokémon with Sabrina in its name. At the end of your turn, discard Sabrina's ESP. If that Pokémon uses and attack that involves flipping coins, Sabrina's ESP lets you re-flip those coins once. If you do, re-flip all the coins.
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="f466c6f3-4782-52c0-b0c3-aa3b1963e120",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.SabrinasESP.Name",
    display_name="Sabrina's ESP",
    searchable_by=["Sabrina's ESP"],
    subtypes=[],
    collector_number=117,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
