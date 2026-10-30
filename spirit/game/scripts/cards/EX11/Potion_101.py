"""STUB: effect not implemented — do not guess mechanics.
Potion (EX11 #101): trainer effect stubbed.

Card text:
  - Remove 2 damage counters from 1 of your Pokémon (remove 1 damage counter if that Pokémon has only 1).
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="e177a6ce-6304-5b1f-bd7d-eb2a4d1edddd",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Potion.Name",
    display_name="Potion",
    searchable_by=["Potion", "Item"],
    subtypes=["Item"],
    collector_number=101,
    set_code="EX11",
    rarity=Rarities.Common,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
