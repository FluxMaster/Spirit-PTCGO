"""STUB: effect not implemented — do not guess mechanics.
Brock's Protection (GYM2 #101): trainer effect stubbed.

Card text:
  - Attach Brock's Protection to 1 of your Pokémon with Brock in its name. Energy cards attached to that Pokémon can't be removed by your opponent's attacks or Trainer cards. (This doesn't stop the rest of the attack or Trainer card from working normally.)
"""

from spirit.game.data_utils import ItemCardDef, unimplemented
from spirit.game.attributes import Rarities

card = ItemCardDef(
    guid="9ed498bf-e15e-5592-9623-f8272c4bb34c",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BrocksProtection.Name",
    display_name="Brock's Protection",
    searchable_by=["Brock's Protection"],
    subtypes=[],
    collector_number=101,
    set_code="GYM2",
    rarity=Rarities.Rare,
    # STUB: trainer effect not implemented
    effect=unimplemented
)
